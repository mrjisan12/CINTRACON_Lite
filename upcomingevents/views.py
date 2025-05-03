from django.shortcuts import render, redirect
from .models import UpcomingEvent
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def upcomingevents(request):
    events = UpcomingEvent.objects.all()
    return render(request,'UpComingEvents/upComingEvents.html',{"events":events})

@login_required
def create_upcoming_event(request):
    if request.method == 'POST':
        title = request.POST.get('title', '')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        date = request.POST.get('date')
        
        
        if not title or not description or not image or not date:
            messages.error(request, "All fields are required!")
            return redirect('upcomingevents')


        UpcomingEvent.objects.create(
            user=request.user,
            title=title,
            description=description,
            image=image,
            date=date,
        )
        messages.success(request, "Upcoming Event created successfully.")
        return redirect('upcomingevents')
    return redirect('upcomingevents')
