from django.urls import path
from . import views

urlpatterns = [
    path('', views.jobopportunities, name="jobopportunities"),
    path('jobs/create/', views.create_job_post, name='create_job_post'),
    path('job/delete/<int:job_id>/', views.delete_job_post, name='delete_job_post'),

]
