from django.forms import ModelForm
from study_tracker.models import AssignmentRecord
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AssignmentRecordForm(ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = AssignmentRecord
        fields = ["name", "subject", "date", "progress", "description"]

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].widget.attrs.update({'class': 'form-control'})

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label="Username", 
                                widget=forms.TextInput(attrs={'placeholder': '150 characters or fewer', 'size': '23', 'class': 'form-control'}),
                                error_messages={'required': 'Please enter your username'})
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'At least 8 characters', 'size': '23', 'class': 'form-control'}))
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password again', 'size': '23', 'class': 'form-control'}))