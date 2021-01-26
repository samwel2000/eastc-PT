from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from accounts.models import *

class FieldScheduleForm(forms.ModelForm):
    class Meta:
        model = FieldSchedule
        exclude = ['created_date']
        widgets = {
            'from_date': forms.DateInput(
            attrs = {
                'type':'date',
                'required':'true'
                }
            ),
            'to_date': forms.DateInput(
            attrs = {
                'type':'date',
                'required':'true'
                }
            ),
            'study_year': forms.TextInput(
            attrs = {
                'required':'true',
                'placeholder':'Example 2019/2020'
            }
            )
        }

class ArrivalUploadForm(forms.ModelForm):
    class Meta:
        model = ArrivalNote
        fields = ['pdf']
        widgets = {
            'pdf': forms.FileInput(
                attrs = {
                    'required':'true',
                    'class':'custom-file-input'
                }
            )
        }


class AddFieldPlaceForm(forms.ModelForm):
    class Meta:
        model = FieldPlace
        fields = ['company_name', 'branch',
                  'department', 'region',
                  'location', 'supervisor_name',
                  'position', 'email']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task','lesson','hours']
        widgets = {
            'task':forms.Textarea(
            attrs = {
                'cols':55,
                'rows':2
            }
            ),
            'lesson':forms.Textarea(
            attrs = {
                'cols':55,
                'rows':2
            }
            ),
        }



class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['program','phone','role_name']
