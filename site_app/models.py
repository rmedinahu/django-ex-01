from django.db import models


class Recruit(models.Model):
	fname = models.CharField(max_length=128)
	age = models.IntegerField()


class Job(models.Model):
	title = models.CharField(max_length=128)
	salary = models.IntegerField()


class RecruitJob(models.Model):
	"""An association between recruit and job objects
	"""
	recruit = models.ForeignKey(Recruit, on_delete=models.CASCADE, related_name='jobs')
	job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='recruits')
	preference = models.IntegerField()


