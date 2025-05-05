from django.db import models
from authentication.models import *

# Create your models here.
class UpcomingEvent(models.Model):
    
   
    
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='upcomingevents/', blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True,null=True,blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='upcoming_events')
    
    
    def __str__(self):
        return f"{self.title} - {self.user.full_name}"

