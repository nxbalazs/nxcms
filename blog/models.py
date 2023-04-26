from django.db import models

# Create your models here.
class BlogTags(models.Model):
    tag = models.CharField(max_length=50, unique=True)

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    tags = models.ManyToManyField('BlogTags', related_name='blogpost')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
