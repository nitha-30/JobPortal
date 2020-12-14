from django.db import models
from django.contrib.auth.models import User

class JobPost(models.Model):
    user=models.CharField(max_length=150)
    company_name=models.CharField(max_length=150)
    job_role=models.CharField(max_length=150)
    skills=models.CharField(max_length=150)
    experience=models.IntegerField()
    location=models.CharField(max_length=150)

    def __str__(self):
        return str(self.user)

