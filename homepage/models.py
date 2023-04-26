from django.db import models

# Create your models here.
class HomepageBody(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

class PageSettings(models.Model):
    name = models.CharField(max_length=50, default='nxcms')
    footer_text = models.CharField(max_length=200, default='Created by Balázs Nagy - 2023')

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)