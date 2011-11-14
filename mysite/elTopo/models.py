from django.db import models

class Index(models.Model):
	"""index model"""
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=50)

	def __unicode__(self):
		return self.title


class PlaceIndex(models.Model):
	"""DetailIndex model"""
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=50)
	
	class Meta:
		db_table = 'place_name'
		ordering = ('title',)
	
	def __unicode__(self):
		return self.title
		

class Place(models.Model):
	"""detail model"""
	name = models.CharField(max_length=255)
	#hours = models.DateTimeField
	url = models.URLField(blank=True, verify_exists=False)
	img = models.CharField(max_length=50)
	slug = models.SlugField(max_length=50)
	
	def __unicode__(self):
		return self.name
		
class About(models.Model):
	"""About Model"""
	title = models.CharField(max_length=255)
	content = models.TextField(blank=True)
	slug = models.SlugField(max_length=50)
	
	def __unicode(self):
		return self.title

class Map(models.Model):
	"""Map Model"""
	title = models.CharField(max_length=255)
	#locations = models.
	slug = models.SlugField(max_length=50)
	
	def __unicode(self):
		return self.title
	
class MapDetail(models.Model):
	"""Map Detail Model"""
	title = models.CharField(max_length=255)
	#location = models.
	slug = models.SlugField(max_length=50)

	def __unicode(self):
		return self.title