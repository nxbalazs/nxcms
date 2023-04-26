from django.db import models

# Create your models here.
class HomepageBody(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)