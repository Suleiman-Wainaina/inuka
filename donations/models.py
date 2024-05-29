from django.db import models

class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class University(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

class Donation(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

class Transaction(models.Model):
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE)
    payment_details = models.TextField()
    status = models.CharField(max_length=20)

