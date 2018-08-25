from django.db import models

# Create your models here.

class contact(models.Model):
	name=models.CharField(max_length=100)
	phone=models.CharField(max_length=15)
	email=models.EmailField(max_length=70,blank=True, unique= True)


	def __str__(self):
		return self.name
