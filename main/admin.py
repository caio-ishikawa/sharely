from django.contrib import admin
from .models import File, Folder, Comment

admin.site.register(File)
admin.site.register(Folder)
admin.site.register(Comment)
