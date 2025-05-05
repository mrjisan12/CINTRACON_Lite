from django.shortcuts import render, redirect
from .models import UpcomingEvent
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def upcomingevents(request):
    events = UpcomingEvent.objects.all().order_by('-created_at')
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


@login_required
def delete_upcoming_event(request, event_id):
    try:
        event = UpcomingEvent.objects.get(id=event_id)

        # Optional: Ensure that only the creator can delete the event
        if event.user != request.user:
            messages.error(request, "You are not authorized to delete this event.")
            return redirect('upcomingevents')

        event.delete()
        messages.success(request, "Event deleted successfully.")
    except UpcomingEvent.DoesNotExist:
        messages.error(request, "Event not found.")
    
    return redirect('upcomingevents')



@login_required
def update_upcoming_event(request, event_id):
    try:
        event = UpcomingEvent.objects.get(id=event_id)

        # Optional: Only the creator can update the event
        if event.user != request.user:
            messages.error(request, "You are not authorized to edit this event.")
            return redirect('upcomingevents')

        if request.method == 'POST':
            title = request.POST.get('title')
            description = request.POST.get('description')
            date = request.POST.get('date')
            image = request.FILES.get('image')

            if not title or not description or not date:
                messages.error(request, "Title, description, and date are required.")
                return redirect('upcomingevents')

            # Update fields
            event.title = title
            event.description = description
            event.date = date

            # Only update image if new one is uploaded
            if image:
                event.image = image

            event.save()
            messages.success(request, "Event updated successfully.")
            return redirect('upcomingevents')

    except UpcomingEvent.DoesNotExist:
        messages.error(request, "Event not found.")

    return redirect('upcomingevents')

