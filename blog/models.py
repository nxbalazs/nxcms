from django.db import models

# Create your models here.
class BlogTags(models.Model):
    tag = models.CharField(max_length=50)