from .models import CollaborateRequest
from django import forms

class CollaborateForm(forms.ModelForm):
    model = CollaborateRequest
    fields = ('name', 'email', 'message')
