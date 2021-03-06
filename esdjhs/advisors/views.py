from django.shortcuts import render
from search_indexes import AdvisorIndex
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D

def first_name_search(request, first_name):
    context = dict(first_name=first_name)
    san_diego = Point(32.7153292, -117.15725509999999)
    # Within a two miles.
    max_dist = D(mi=200)
    context['advisors'] = AdvisorIndex.objects.filter(first_name=first_name).dwithin('location', san_diego, max_dist)[:5]
    return render(request, 'advisors/first_name_search.html', context)