from django import forms
from django.contrib.auth.models import User
from .models import Movie,Rating
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
class SignUpForm(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'first_name':'First Name','last_name':'Last Name','email':'Email Address'}
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }

class AddMovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields='__all__'
        labels={'title':'Movie Title','image':'','movieduration':'Duration'}
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'genres':forms.TextInput(attrs={'class':'form-control'}),
            'year':forms.TextInput(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
            'movieduration':forms.TextInput(attrs={'class':'form-control'})
        }

class LoginForm(AuthenticationForm):
    username=forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        fields=['username','password']


class AddRatingForm(forms.ModelForm):
  
    class Meta:
        model=Rating
        fields=['rating']
        labels={'rating':'Rating'}
        widgets={
            'rating':forms.TextInput(attrs={'type':'range','step':'1','min':'0','max':'5','class':{'custom-range','border-0'}})
        }
