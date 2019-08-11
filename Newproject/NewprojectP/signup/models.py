from django.db import models

class signup(models.Model):
	name = models.CharField(max_length=50, unique=False)
	email = models.EmailField()
	password = models.CharField(max_length=25)

	def __str__(self):
		return self.name