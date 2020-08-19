from django import forms
from django.forms import CheckboxSelectMultiple

from webapp.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = []
        widgets = {
            'types': CheckboxSelectMultiple,
        }


class SearchForm(forms.Form):
    search = forms.CharField(max_length=50, required=False, label='Search')