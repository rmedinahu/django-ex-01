from django.test import TestCase

from .models import Recruit, Job, RecruitJob

class RecruitsTestCase(TestCase):

    def setup(self):
        r = Recruit(fname='richie', age=33)
        r.save()

        r = Recruit(fname='adrian', age=37)
        r.save()

        r = Recruit(fname='isaac', age=43)
        r.save()

        j = Job(title='programmer', salary=30000)
        j.save()

        j = Job(title='software analyst', salary=90000)
        j.save()

        recruits = Recruit.objects.all()
        jobs = Job.objects.all()

        rj = RecruitJob(recruit=recruits[0], job=jobs[0], preference=5)
        rj.save()
        
        rj = RecruitJob(recruit=recruits[0], job=jobs[1], preference=4)
        rj.save()

        rj = RecruitJob(recruit=recruits[2], job=jobs[1], preference=10)
        rj.save()

    def test_recruit_job_pairs(self):
        self.setup()
        richie = Recruit.objects.get(fname='richie')
        richies_jobs = richie.jobs.all()

        adrian = Recruit.objects.get(fname='adrian')
        adrians_jobs = adrian.jobs.all()

        self.assertEqual(len(richies_jobs), 2)
        self.assertEqual(len(adrians_jobs), 0)















