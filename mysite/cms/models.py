from django.db import models

class Pub(models.Model):
	title = models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.title
		
class Pages(models.Model):
	tagline = models.CharField(max_length=50)
	url = models.CharField(max_length=100)
	hours = models.CharField(max_length=50)
	content = models.TextField(blank="True")
	
	def __unicode__(self):
		return self.tagline
	