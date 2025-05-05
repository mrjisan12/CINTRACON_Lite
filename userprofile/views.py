from django.shortcuts import render, redirect, get_object_or_404
from authentication.models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
        messages.error(request, "You don't have permission to edit this profile.")
        return redirect('profile', id=user.id)
    
    # Handle POST request with both forms
    if request.method == 'POST':
        print(request.POST)
        user_form = CustomUserForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user.userprofile)
        
        if user_form.is_valid() and profile_form.is_valid():
            try:
                user_form.save()  # Save changes to CustomUser
                profile_form.save()  # Save changes to UserProfile
                messages.success(request, "Profile updated successfully!")
                return redirect('profile', id=user.id)
            except Exception as e:
                messages.error(request, f"An error occurred while saving: {str(e)}")
        else:
            # Form validation errors
            for field, errors in user_form.errors.items():
                for error in errors:
                    messages.error(request, f"User form error - {field}: {error}")
            for field, errors in profile_form.errors.items():
                for error in errors:
                    messages.error(request, f"Profile form error - {field}: {error}")
    else:
        user_form = CustomUserForm(instance=user)
        profile_form = UserProfileForm(instance=user.userprofile)
    
    context = {
        'user': user,
        'user_form': user_form,
        'profile_form': profile_form
    }
    
    return render(request, 'ProfilePage/edit_profile.html', context)
