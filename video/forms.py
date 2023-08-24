from dataclasses import fields
from pyexpat import model
from tkinter.ttk import Widget
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm 
from django.forms import ModelForm
from django import forms
from .models import *



class UserForm(ModelForm):
    class Meta:
        model=User
        fields=['username','email']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class RateForm(forms.ModelForm):

    class Meta:
        model = ReviewRating
        fields= '__all__'

        
class CommentForm(forms.ModelForm):
    commenter = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
    'class':'form-control', 'placeholder':'your name'}))
    body = forms.CharField(max_length=100, widget= forms.Textarea(attrs={
        'class' : 'form-control', 'placeholder' : 'comment here', 'rows' : 3 }))
    
    class Meta:
        model = Comment
        fields = ['commenter','body']

class PasswordChangingForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
    new_password1 = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # class Meta:
    #     model=User
    #     fields=['old_password','new_password1','new_password2']
        

# class PasswordChangingForm(forms.Form):
    
#     class Meta:
#         model=User
#         fields=['old_password','new_password1','new_password2']

# class CommentsForm(forms.ModelForm):

#     class Meta:
#         model = Comments
#         fields = ('comment',)
#         widgets = {
#           'comments': forms.Textarea(attrs={'rows':5, 'cols':40}),
#         }