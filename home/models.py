from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=400)
    desc = models.TextField()
    author = models.CharField(max_length=20)
    published = models.DateField()
    file = models.FileField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return self.title

class Comments(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comments = models.TextField()
    blog  = models.ForeignKey('Blog',on_delete=models.CASCADE, blank=True,null=True)
    created_at = models.DateField(auto_now_add=True)