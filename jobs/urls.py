from django.urls import path
from . import views
from .views import JobListView, JobDetailView, ApplicationDetailView

urlpatterns = [ 
    path('', JobListView.as_view(), name='job_list'),
    path('jobs/<int:pk>/', JobDetailView.as_view(), name='job_detail'),
    path('jobs/<int:pk>/apply/', views.job_apply, name='job_apply'),
    path('applications/', views.applications, name='applications'),
    path('employer_jobs/', views.EmployerJobsView.as_view(), name='employer_jobs'),
    path('employer_jobs/add/', views.JobCreateView.as_view(), name='add_job'),
    path('employer_jobs/<int:pk>/edit/', views.JobUpdateView.as_view(), name='edit_job'),
    path('employer_jobs/<int:pk>/delete/', views.JobDeleteView.as_view(), name='delete_job'),
    path('applications/<int:pk>/', ApplicationDetailView.as_view(), name='application_detail'),
    path('applications/<int:pk>/withdraw/', views.ApplicationWithdrawView.as_view(), name='withdraw_application'),
]  