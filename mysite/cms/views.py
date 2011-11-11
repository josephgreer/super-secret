from django.template import Context, loader
from django.http import HttpResponse
from cms.models import Pub
from django.shortcuts import render_to_response

def index(request):
	pubs_list = Pub.objects.all()
	return render_to_response('cms/base.html', {'pubs_list' : pubs_list })
		
def detail(request, pub_id):
	pub = Pub.objects.get(pk=pub_id)
	return render_to_response('cms/pub_detail.html', { 'pub': pub })