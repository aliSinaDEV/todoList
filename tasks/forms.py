from django import forms
from django.forms import ModelForm
from . models import *

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'form1', 'placeholder': 'Enter a task here'}))
    priority = forms.ChoiceField(choices=((1, 'Low Priority'), (2, 'Middle Priority'), (3, 'High Priority')), widget=forms.Select(attrs={'class': 'form-select', 'aria-label': 'Default select example'}))
    
    class Meta:
        model = Task
        fields = ['title', 'priority', 'complete']
