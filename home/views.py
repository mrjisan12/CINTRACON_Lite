from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
from .forms import *

# Create your views here.
def home(request):
    posts = Post.objects.all().order_by('-created_at')  
    return render(request, 'HomePage/homePage.html', {'posts': posts})


@login_required
def create_post(request):
    if request.method == 'POST':
        content = request.POST.get('content', '')
        image = request.FILES.get('image')
        video = request.FILES.get('video')

        if not content and not image and not video:
            messages.error(request, "Post cannot be empty!")
            return redirect('home')

        Post.objects.create(
            user=request.user,
            content=content,
            image=image,
            video=video
        )
        messages.success(request, "Post created successfully.")
        return redirect('home')
    return redirect('home')

@login_required
def add_comment(request, post_id):
    if request.method == 'POST':
        text = request.POST.get('comment')
        if text:
            Comment.objects.create(user=request.user, post_id=post_id, text=text)
    return redirect('home')

@login_required
def react_to_post(request, post_id, reaction_type):
    post = Post.objects.get(pk=post_id)
    existing_reaction = Reaction.objects.filter(user=request.user, post=post).first()

    if existing_reaction:
        existing_reaction.type = reaction_type
        existing_reaction.save()
    else:
        Reaction.objects.create(user=request.user, post=post, type=reaction_type)

    return redirect('home')


@login_required
def user_profile(request, id):
    user = get_object_or_404(CustomUser,id=id)
    return render(request,'ProfilePage/profile.html',{'user':user})


@login_required
def edit_profile(request, id):
    user = get_object_or_404(CustomUser, id=id)
    
    # Check if the logged in user is editing their own profile
    if request.user.id != user.id:
        return redirect('profile', id=user.id)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile', id=user.id)
    else:
        form = UserProfileForm(instance=user)
    
    context = {
        'user': user,
        'form': form
    }
    return render(request, 'ProfilePage/edit_profile.html', context)