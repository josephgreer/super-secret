from django.http import HttpResponse
from elTopo.models import *
from django.shortcuts import render_to_response


def index(request):
	app_places = Place.objects.all()[:4]
	return render_to_response('elTopo/home.html', { 'app_places' : app_places })

def placeIndex(request):
	app_places = Place.objects.all()
	return render_to_response('elTopo/places.html', { 'app_places' : app_places })
	
def place(request, place_id):
	detail = Place.objects.get(place_id)
	return render_to_response('elTopo/place_detail.html', {'detail' : detail })
	