from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class Item(models.Model):
	name = models.CharField(max_length=50)
	category = models.ForeignKey(Category, on_delete=None)
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return self.name
