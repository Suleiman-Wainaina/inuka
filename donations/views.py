from django.shortcuts import render, redirect
from .forms import VolunteerForm, DonationForm
from .models import University, Donation
from django.core.mail import send_mail

def home(request):
    universities = University.objects.all()
    return render(request, 'donations/home.html', {'universities': universities})

def donate(request):
    if request.method == 'POST':
        volunteer_form = VolunteerForm(request.POST)
        donation_form = DonationForm(request.POST)
        if volunteer_form.is_valid() and donation_form.is_valid():
            volunteer = volunteer_form.save()
            donation = donation_form.save(commit=False)
            donation.volunteer = volunteer
            donation.save()
            # Send confirmation email
            send_mail(
                'Thank You for Your Donation',
                'Dear {},\n\nThank you for donating {} to {}.\n\nBest regards,\nInuka Team'.format(
                    volunteer.name, donation.amount, donation.university.name),
                'from@example.com',
                [volunteer.email],
                fail_silently=False,
            )
            return redirect('thank_you')
    else:
        volunteer_form = VolunteerForm()
        donation_form = DonationForm()
    return render(request, 'donations/donate.html', {'volunteer_form': volunteer_form, 'donation_form': donation_form})

def thank_you(request):
    return render(request, 'donations/thank_you.html')

from paypal.standard.forms import PayPalPaymentsForm

def donate(request):
    if request.method == 'POST':
        volunteer_form = VolunteerForm(request.POST)
        donation_form = DonationForm(request.POST)
        if volunteer_form.is_valid() and donation_form.is_valid():
            volunteer = volunteer_form.save()
            donation = donation_form.save(commit=False)
            donation.volunteer = volunteer
            donation.save()
            # PayPal integration
            paypal_dict = {
                "business": settings.PAYPAL_RECEIVER_EMAIL,
                "amount": donation.amount,
                "item_name": "Donation for {}".format(donation.university.name),
                "invoice": str(donation.id),
                "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
                "return_url": request.build_absolute_uri(reverse('thank_you')),
                "cancel_return": request.build_absolute_uri(reverse('donate')),
            }
            form = PayPalPaymentsForm(initial=paypal_dict)
            context = {
                "form": form,
                "volunteer_form": volunteer_form,
                "donation_form": donation_form,
            }
            return render(request, 'donations/donate.html', context)
    else:
        volunteer_form = VolunteerForm()
        donation_form = DonationForm()
    return render(request, 'donations/donate.html', {'volunteer_form': volunteer_form, 'donation_form': donation_form})


from .models import University, Donation
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
