from django import forms
from .models import Volunteer, Donation

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['name', 'email']

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['university', 'amount']
