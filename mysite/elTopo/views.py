from django.http import HttpResponse
from models.elTopo import *

def placeIndex(request):
	app_places = Places.objects.all()
	return render_to_response('elTopo/places.html', { 'app_places' : app_places})
	