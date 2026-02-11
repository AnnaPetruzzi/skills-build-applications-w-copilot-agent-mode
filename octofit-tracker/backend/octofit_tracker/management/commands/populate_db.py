from django.core.management.base import BaseCommand
from octofit_tracker.models import User  # Adjust import as needed for your models

class Command(BaseCommand):
    help = 'Populates the database with initial data for Octofit Tracker.'

    def handle(self, *args, **options):
        # Example: Create a default user if none exist
        if not User.objects.exists():
            User.objects.create(username='octofit_admin', email='admin@octofit.com')
            self.stdout.write(self.style.SUCCESS('Created default user: octofit_admin'))
        else:
            self.stdout.write(self.style.WARNING('Users already exist. No new user created.'))
