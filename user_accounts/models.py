from django.db import models
from django.contrib.auth.models import User

# UserType model
class UserType(models.Model):
    # Choices for user type
    user_types = (
        ('job_applicant', 'Job Applicant'),
        ('employer', 'Employer'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)  # One-to-one relationship with the User model
    user_type = models.CharField(max_length=20, choices=user_types)  # User type field