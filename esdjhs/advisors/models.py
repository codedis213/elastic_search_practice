from django.db import models
from django.contrib.gis.geos import Point

class Company(models.Model):
    company_name = models.CharField(max_length=256)
    doing_business_as_name = models.CharField(max_length=256)
    full_address = models.CharField(max_length=256)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)

    @property
    def geo_location(self):
        return Point(self.longitude, self.latitude) if self.latitude and self.longitude else None

    def __unicode__(self):
        return self.company_name


class Advisor(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    crd = models.IntegerField()  # SEC unique id
    company = models.ForeignKey(Company)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)


    def __unicode__(self):
        return "({crd}) {fn} {ln}".format(crd=self.crd, fn=self.first_name, ln=self.last_name)
