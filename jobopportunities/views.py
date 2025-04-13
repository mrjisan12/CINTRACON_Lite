from django.shortcuts import render
from .models import JobPost

# Create your views here.
def jobopportunities(request):
    jobs = JobPost.objects.all()
    return render(request,'JobOpportunities/jobOpp.html',{"jobs":jobs})