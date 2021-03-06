import celery_geolocator
from celery_geolocator.tasks import geocode
from django.core.management import BaseCommand

from advisors.models import Company


__author__ = 'brentpayne'

class Command(BaseCommand):
    help = """
      This script uses the Nominatim geocoder to geocode as many company addresses as possible.

      Example:
        python manage.py geocode_companies
    """

    def handle(self, *args, **options):
        for company in Company.objects.filter(latitude__isnull=True):
            error, formatted_address, point, raw, type = geocode(company.full_address, celery_geolocator.NOMINATIM_GEOCODER)
            if point and len(point)>1:
                company.latitude = point[0]
                company.longitude = point[1]
                company.save()