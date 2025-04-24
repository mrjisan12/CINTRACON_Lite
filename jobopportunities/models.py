from django.db import models
from django.contrib.auth.models import User 
from authentication.models import *

# Create your models here.
class JobPost(models.Model):
    
    
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    company_name = models.CharField(max_length=100)
    salary = models.IntegerField()
    place = models.CharField(max_length=100)
    start_timing = models.TimeField(max_length=50,null=True,blank=True)
    end_timing = models.TimeField(max_length=50,null=True,blank=True)
    apply_link = models.CharField(max_length=200)
    image = models.ImageField(upload_to='jobPost/', blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='job_posts')
    
    
    def __str__(self):
        return f"{self.title} - {self.user.username}"