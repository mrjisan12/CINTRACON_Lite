from django.shortcuts import render
from authentication.models import UserProfile
from django.db.models import Q

# def allStudents(request):
#     students = UserProfile.objects.select_related('user').filter(user__is_superuser=False)
#     return render(request, 'AllStudents/allStudentsPage.html', {'students': students})


def allStudents(request):
    query = request.GET.get('q', '')
    
    students = UserProfile.objects.select_related('user').filter(
        user__is_superuser=False
    )
    
    if query:
        students = students.filter(
            Q(user__full_name__icontains=query) |
            Q(department__icontains=query) |
            Q(section__icontains=query) |
            Q(batch_no__icontains=query)
        )
    
    # For HTMX requests, return only the students grid
    if request.headers.get('HX-Request'):
        return render(request, 'AllStudents/student_grid.html', {
            'students': students,
            'query': query
        })
    
    return render(request, 'AllStudents/allStudentsPage.html', {
        'students': students,
        'query': query
    })