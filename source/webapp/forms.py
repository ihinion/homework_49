from django import forms
from django.forms import widgets
from webapp.models import Status, Type


class TaskForm(forms.Form):
    description = forms.CharField(max_length=200, label='Description', required=True)
    detailed_desc = forms.CharField(max_length=1500, label='Detailed description', required=False,
                                    widget=widgets.Textarea)
    status = forms.ModelChoiceField(label='Status', required=True, queryset=Status.objects.all(),
                                    initial=Status.objects.get(name__iexact='new'))
    type = forms.ModelChoiceField(label='Type', required=True, queryset=Type.objects.all(),
                                  initial=Type.objects.get(name__iexact='task'))
