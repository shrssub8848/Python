from django.db import models

# Create your models here.
class Introduction(models.Model):
	name= models.CharField(max_length=50,unique=True)# need memory for string not for integer
	age = models.IntegerField()
	number = models.IntegerField()


class Python(models.Model):
	Session = models.CharField(max_length=20,unique=True)


class Student1(models.Model):
	name = models.CharField(max_length=20,unique=False)
	Session = models.ForeignKey("Python", on_delete=models.PROTECT)

class signup(models.Model):
	name = models.CharField(max_length=50, unique=False)
	email = models.EmailField()
	password = models.CharField(max_length=25)

	def __str__(self):
		return self.name