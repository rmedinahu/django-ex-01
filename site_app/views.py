from django.shortcuts import render

# generic views - see more at https://docs.djangoproject.com/en/2.1/ref/class-based-views/
from django.views import generic

from .models import Recruit, Job, RecruitJob

class HomeView(generic.TemplateView):
	# Inherits from TemplateView (gets a function as_view())
	template_name = 'index.html'


class RecruitView(generic.DetailView):
	model = Recruit
	template_name = 'recruit.html'

	def get_context_data(self, **kwargs):
		context = super(RecruitView, self).get_context_data(**kwargs)
		recruit_obj = self.get_object()

		context['jobs'] = recruit_obj.jobs.all().order_by('preference')
		return context


class RecruitListView(generic.ListView):
	model = Recruit
	template_name = 'recruit_list.html'


class JobView(generic.DetailView):
	model = Job
	template_name = 'job.html'

	def get_context_data(self, **kwargs):
		context = super(JobView, self).get_context_data(**kwargs)
		job_obj = self.get_object()

		context['recruits'] = job_obj.recruits.all().order_by('recruit__fname')
		return context


class JobListView(generic.ListView):
	model = Job
	template_name = 'job_list.html'









