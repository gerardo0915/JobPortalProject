from django.db import models
from django.contrib.auth.models import User

class UserType(models.Model):
    user_types = (
        ('job_applicant', 'Job Applicant'),
        ('employer', 'Employer'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=user_types)