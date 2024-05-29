from django.core.management.base import BaseCommand
from donations.models import University

class Command(BaseCommand):
    help = 'Populate the University model with initial data'

    def handle(self, *args, **kwargs):
        universities = [
            {"name": "University of Nairobi", "location": "Nairobi"},
            {"name": "Kenyatta University", "location": "Nairobi"},
            {"name": "Moi University", "location": "Eldoret"},
            {"name": "Egerton University", "location": "Njoro"},
            {"name": "Jomo Kenyatta University of Agriculture and Technology", "location": "Juja"},
            # Add more universities as needed
        ]
        for uni in universities:
            University.objects.create(**uni)
        self.stdout.write(self.style.SUCCESS('Successfully populated universities'))
