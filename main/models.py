from django.db import models
from django.contrib.auth.models import User


class File(models.Model):
    file = models.FileField(upload_to='files/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Folder(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.ManyToManyField(File, related_name='files', blank=True)
    allowed_user = models.ManyToManyField(User, related_name='allowed_users', blank=True)

    def __str__(self):
        return self.name


class Link(models.Model):
    key = models.CharField(primary_key=True, max_length=50)
    folder = models.ForeignKey(Folder, unique=True, on_delete=models.CASCADE)


class Comment(models.Model):
    comment_folder = models.ForeignKey(Folder, related_name='comments', on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True)
