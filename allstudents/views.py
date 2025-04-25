from django.shortcuts import render
from authentication.models import UserProfile

def allStudents(request):
    students = UserProfile.objects.select_related('user').filter(user__is_superuser=False)
    return render(request, 'AllStudents/allStudentsPage.html', {'students': students})
