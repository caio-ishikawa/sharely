from django import forms
from django.forms import ModelForm
from .models import File, Folder, Comment
from crispy_forms.helper import FormHelper


class FileForm(ModelForm):
    class Meta:
        model = File
        fields = ('file', 'title',)


class FolderForm(ModelForm):
    class Meta:
        model = Folder
        fields = ('name', 'file',)

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
