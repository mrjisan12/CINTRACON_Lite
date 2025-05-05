from django import forms
from authentication.models import *


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['full_name']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'w-full bg-white/10 border border-purple-400/60 text-white rounded-lg px-4 py-2.5 focus:outline-none focus:ring-2 focus:ring-purple-400 shadow-inner shadow-purple-300/20',
                'required': True
            }),
            
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'profile_image',
            'batch_no',
            'blood_grp',
            'department',
            'semester',
            'section',
            'facebook_link',
            'linkedin_link',
            'instagram_link'
        ]
        widgets = {
            'profile_image': forms.FileInput(attrs={
                'class': 'hidden',
                'accept': 'image/*'
            }),
            'batch_no': forms.TextInput(attrs={
                'class': 'w-full bg-white/10 border border-purple-400/60 text-white rounded-lg px-4 py-2.5 focus:outline-none focus:ring-2 focus:ring-purple-400 shadow-inner shadow-purple-300/20',
                'required': True
            }),
            'blood_grp': forms.Select(attrs={
                'class': 'w-full bg-transparent border border-purple-400/60 text-white rounded-lg px-4 py-2.5 focus:outline-none focus:ring-2 focus:ring-purple-400 shadow-inner shadow-purple-300/20'
            }),
            'department': forms.Select(attrs={
                'class': 'w-full bg-transparent border border-purple-400/60 text-white rounded-lg px-4 py-2.5 focus:outline-none focus:ring-2 focus:ring-purple-400 shadow-inner shadow-purple-300/20'
            }),
            'semester': forms.Select(attrs={
                'class': 'w-full bg-transparent border border-purple-400/60 text-white rounded-lg px-4 py-2.5 focus:outline-none focus:ring-2 focus:ring-purple-400 shadow-inner shadow-purple-300/20'
            }),
            'section': forms.Select(attrs={
                'class': 'w-full bg-transparent border border-purple-400/60 text-white rounded-lg px-4 py-2.5 focus:outline-none focus:ring-2 focus:ring-purple-400 shadow-inner shadow-purple-300/20'
            }),
            'facebook_link': forms.URLInput(attrs={
                'class': 'w-full bg-white/10 border border-purple-400/60 text-white rounded-lg px-4 py-2.5 focus:outline-none focus:ring-2 focus:ring-purple-400 shadow-inner shadow-purple-300/20',
                'placeholder': 'https://facebook.com/username'
            }),
            'linkedin_link': forms.URLInput(attrs={
                'class': 'w-full bg-white/10 border border-purple-400/60 text-white rounded-lg px-4 py-2.5 focus:outline-none focus:ring-2 focus:ring-purple-400 shadow-inner shadow-purple-300/20',
                'placeholder': 'https://github.com/username'
            }),
            'instagram_link': forms.URLInput(attrs={
                'class': 'w-full bg-white/10 border border-purple-400/60 text-white rounded-lg px-4 py-2.5 focus:outline-none focus:ring-2 focus:ring-purple-400 shadow-inner shadow-purple-300/20',
                'placeholder': 'https://instagram.com/username'
            })
        }