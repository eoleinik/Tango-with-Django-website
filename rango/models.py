from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	slug = models.SlugField(default=0)

        def save(self, *args, **kwargs):
                self.slug = slugify(self.name)
                self.views = max(self.views, 0)
                self.likes = max(self.likes, 0)
                super(Category, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.name

class Page(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=128)
	url = models.URLField()
	views = models.IntegerField(default=0)

	def __unicode__(self):
		return self.title

class UserProfile(models.Model):
	user = models.OneToOneField(User)

	website = models.URLField(blank = True)
	picture = models.ImageField(upload_to='profile_images', blank=True)

	def __unicode__(self):
		return self.user.username