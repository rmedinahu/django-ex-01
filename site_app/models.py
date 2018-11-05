from django.db import models


class Recruit(models.Model):
	fname = models.CharField(max_length=128)
	age = models.IntegerField()

