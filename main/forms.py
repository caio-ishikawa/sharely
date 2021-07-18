from django import forms
from django.forms import ModelForm
from .models import File, Folder


class FileForm(ModelForm):
    class Meta:
        model = File
        fields = ('file', 'title',)


class FolderForm(ModelForm):
    class Meta:
        model = Folder
        fields = ('name', 'file',)
