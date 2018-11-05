from django.shortcuts import render

# generic views - see more at https://docs.djangoproject.com/en/2.1/ref/class-based-views/
from django.views import generic

from .models import Recruit

class HomeView(generic.TemplateView):
	template_name = 'index.html'


class RecruitView(generic.DetailView):
	model = Recruit
	template_name = 'recruit.html'