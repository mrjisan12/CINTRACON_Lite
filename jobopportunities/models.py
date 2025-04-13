from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class JobPost(models.Model):
    
    TIMING = (
        ('9 AM to 5 PM','9 AM to 5 PM'),
        ('10 AM to 4 PM','10 AM to 4 PM'),
        ('10 AM to 12 PM','10 AM to 12 PM'),
        ('2 PM to 8 PM','2 PM to 8 PM'),
    )
    
    
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    company_name = models.CharField(max_length=100)
    salary = models.IntegerField()
    place = models.CharField(max_length=100)
    timing = models.CharField(max_length=50, choices=TIMING)
    apply_link = models.CharField(max_length=200)
    image = models.ImageField(upload_to='jobPost/', blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_posts')
    
    
    def __str__(self):
        return f"{self.title} - {self.user.username}"