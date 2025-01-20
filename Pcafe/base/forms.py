from django import forms

from .models import *

class StudentCreationform(forms.ModelForm):

    class Meta:
        model = StudentData
        fields = ['name','roll','phone','department','email','points','profile_picture']

        