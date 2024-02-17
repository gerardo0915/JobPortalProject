from django.db import models
from django.contrib.auth.models import User 

# Job model
class Job(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # reference to the User model
    job_title = models.CharField(max_length=200)  # job title
    company_name = models.CharField(max_length=200)  # company name
    description = models.TextField()  # job description
    location = models.CharField(max_length=200)  # job location
    deadline = models.DateTimeField()  # application deadline

    def __str__(self):
        return self.job_title  # returns job title when the object is printed

# JobApplication model
class JobApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # reference to the User model
    job = models.ForeignKey(Job, on_delete=models.CASCADE)  # reference to the Job model
    resume = models.FileField(upload_to='resumes/')  # resume file
    additional_comments = models.TextField(null=True, blank=True)  # additional comments
    applied_date = models.DateTimeField(auto_now_add=True)  # date when the application was submitted

    def __str__(self):
        return self.user.username + ' - ' + self.job.job_title 