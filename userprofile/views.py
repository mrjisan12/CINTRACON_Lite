from django.shortcuts import render, redirect, get_object_or_404
from authentication.models import *
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def user_profile(request, id):
    user = get_object_or_404(CustomUser,id=id)
    return render(request,'ProfilePage/profile.html',{'user':user})


@login_required
def edit_profile(request, id):
    user = get_object_or_404(CustomUser, id=id)
    
    # Ensure the logged in user is editing their own profile
    if request.user.id != user.id:
        return redirect('profile', id=user.id)
    
    # Handle POST request with both forms
    if request.method == 'POST':
        user_form = CustomUserForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user.userprofile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()  # Save changes to CustomUser
            profile_form.save()  # Save changes to UserProfile
            return redirect('profile', id=user.id)
    else:
        user_form = CustomUserForm(instance=user)
        profile_form = UserProfileForm(instance=user.userprofile)
    
    context = {
        'user': user,
        'user_form': user_form,
        'profile_form': profile_form
    }
    
    return render(request, 'ProfilePage/edit_profile.html', context)
