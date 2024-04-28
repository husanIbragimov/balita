from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import GetInTouch


class GetInTouchForm(forms.ModelForm):
    class Meta:
        model = GetInTouch
        fields = "__all__"
        execute = ["created_at"]
    
    def __init__(self, *args, **kwargs):
        super(GetInTouchForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

