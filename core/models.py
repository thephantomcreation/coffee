from django.db import models
from django.utils import timezone

class Contact(models.Model):
	name= models.CharField(max_length=75)
	email = models.EmailField()
	message = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)



	def __str__(self):
		return self.email
