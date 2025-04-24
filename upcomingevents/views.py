from django.shortcuts import render
from .models import UpcomingEvent

# Create your views here.
def upcomingevents(request):
    events = UpcomingEvent.objects.all()
    return render(request,'UpComingEvents/upComingEvents.html',{"events":events})

