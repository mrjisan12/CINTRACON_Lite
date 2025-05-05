from django.shortcuts import render, redirect
from .models import JobPost
from django.contrib.auth.decorators import login_required
from .forms import JobPostForm
from django.contrib import messages
from django.shortcuts import get_object_or_404

# Create your views here.
@login_required
def jobopportunities(request):
    jobs = JobPost.objects.all().order_by('-created_at')
    return render(request,'JobOpportunities/jobOpp.html',{"jobs":jobs})


@login_required
def create_job_post(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST, request.FILES)
        if form.is_valid():
            job_post = form.save(commit=False)
            job_post.user = request.user
            job_post.save()
            messages.success(request, "Job posted successfully!")
            return redirect('jobopportunities')
        else:
            messages.error(request, "There was an error with your job post.")
    return redirect('jobopportunities')


@login_required
def delete_job_post(request, job_id):
    job_post = get_object_or_404(JobPost, id=job_id, user=request.user)
    job_post.delete()
    messages.success(request, "Job post deleted successfully!")
    return redirect('jobopportunities')