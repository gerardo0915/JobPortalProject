from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from .models import Job, JobApplication

# Job creation form
class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['job_title', 'company_name', 'description', 'location', 'deadline']
        widgets = {
            'job_title': forms.TextInput(attrs={'class': 'form-control'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'deadline': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

# Job application form 
class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['resume', 'additional_comments']
        widgets = {
            'resume': forms.FileInput(attrs={'class': 'form-control'}),
            'additional_comments': forms.Textarea(attrs={'class': 'form-control'}),
        }
        

