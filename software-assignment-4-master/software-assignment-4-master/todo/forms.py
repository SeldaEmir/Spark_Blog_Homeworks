__author__ = 'seldaemir'

from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ["name", "description", "tags"]