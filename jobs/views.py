from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, DeleteView , CreateView
from .models import Job , JobApplication
from user_accounts.models import UserType
from .forms import JobApplicationForm , JobForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden 
from django.urls import reverse_lazy 

class JobListView(ListView):
    # Show list of all jobs
    model = Job
    template_name = 'job_list.html'
    context_object_name = 'jobs'
    paginate_by = 5
    ordering = ['job_title'] 

    def get_queryset(self):
        queryset = super().get_queryset()
        job_title = self.request.GET.get('job_title')
        if job_title:
            queryset = queryset.filter(job_title__icontains=job_title)
        location = self.request.GET.get('location')
        if location:
            queryset = queryset.filter(location__icontains=location)
        company = self.request.GET.get('company')
        if company:
            queryset = queryset.filter(company_name__icontains=company)
        return queryset    

class JobDetailView(DetailView):
    # Show details of a specific job
    model = Job
    template_name = 'job_detail.html'
    context_object_name = 'job' 

class EmployerJobsView(ListView):
    # Show list of jobs posted by the employer
    model = Job
    template_name = 'employer_jobs.html'
    context_object_name = 'jobs'
    paginate_by = 5
    ordering = ['job_title'] 

    def get_queryset(self): 
        return Job.objects.filter(user=self.request.user)

    def dispatch(self, request, *args, **kwargs): 
        user_type = UserType.objects.get(user=request.user).user_type
        if user_type != 'employer':
            return HttpResponseForbidden("You are not authorized to view this page.")
        return super().dispatch(request, *args, **kwargs)
    
class JobCreateView(CreateView):
    # Create a new job listing    
    model = Job
    form_class = JobForm
    template_name = 'add_job.html'
    success_url = reverse_lazy('employer_jobs')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
 
class JobUpdateView(UpdateView):
    # Update a specific job listing
    model = Job
    form_class = JobForm
    template_name = 'edit_job.html'
    success_url = reverse_lazy('employer_jobs')

class JobDeleteView(DeleteView):
    # Delete a specific job listing
    model = Job
    template_name = 'delete_job.html'
    success_url = reverse_lazy('employer_jobs')

@login_required
def applications(request):
    # Show list of applications for the user
    user_type = UserType.objects.get(user=request.user).user_type
    if user_type == 'employer':
        # If the user is an employer, get all applications for their jobs
        applications = JobApplication.objects.filter(job__user=request.user)
    else:
        # If the user is an applicant, get all their applications
        applications = JobApplication.objects.filter(user=request.user)
    return render(request, 'applications.html', {'applications': applications})

class ApplicationDetailView(DetailView):
    # Show details of a specific application
    model = JobApplication
    template_name = 'application_detail.html'
    context_object_name = 'application' 

class ApplicationWithdrawView(DeleteView):
    # Withdraw a specific application
    model = JobApplication
    template_name = 'withdraw_application.html'
    success_url = reverse_lazy('applications')

@login_required
def job_apply(request, pk):
    # Apply to a specific job
    job = get_object_or_404(Job, pk=pk)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            job_application = form.save(commit=False)
            job_application.user = request.user
            job_application.job = job
            job_application.save()
            return redirect('applications')
    else:
        form = JobApplicationForm()
    return render(request, 'job_apply.html', {'form': form, 'job': job, 'user': request.user})