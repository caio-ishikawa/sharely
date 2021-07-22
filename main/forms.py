from django import forms
from django.forms import ModelForm
from .models import File, Folder, Comment
from crispy_forms.helper import FormHelper


class FileForm(ModelForm):
    class Meta:
        model = File
        fields = ('title', 'file',)


class FolderForm(ModelForm):
    class Meta:
        model = Folder
        fields = ('name',)

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        ordering = ['date',]

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.form_show_errors = False
