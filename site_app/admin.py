from django.contrib import admin

from .models import Recruit, Job, RecruitJob

admin.site.register(Recruit)
admin.site.register(Job)
admin.site.register(RecruitJob)