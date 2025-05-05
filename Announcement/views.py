from django.shortcuts import render
from .models import Announcement
from django.contrib.auth.decorators import login_required

@login_required
def announcement_view(request):
    announcements = Announcement.objects.all().order_by('-date', '-time')  # Optional: latest first
    return render(request, 'Announcement/announcement.html', {'announcements': announcements})
