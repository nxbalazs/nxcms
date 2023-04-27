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
    menu1_text = models.CharField(max_length=50, default='Homepage')
    menu2_text = models.CharField(max_length=50, default='Blog')
    menu3_text = models.CharField(max_length=50, default='Links')
    menu4_text = models.CharField(max_length=50, default='Login')
    menu5_text = models.CharField(max_length=50, default='Logout')
    menu6_text = models.CharField(max_length=50, default='Dashboard')

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)