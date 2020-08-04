from django import forms
from django.forms import widgets
from webapp.models import TYPE_CHOICES, STATUS_CHOICES


class TaskForm(forms.Form):
    description = forms.CharField(max_length=200, label='Description', required=True)
    detailed_desc = forms.CharField(max_length=1500, label='Detailed description', required=False,
                                    widget=widgets.Textarea)
    status = forms.ChoiceField(label='Status', required=True, choices=STATUS_CHOICES,
                               initial=STATUS_CHOICES[0][0])
    type = forms.ChoiceField(label='Type', required=True, choices=TYPE_CHOICES,
                             initial=TYPE_CHOICES[0][0])
