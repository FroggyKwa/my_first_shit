from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth import models as m


class Post(models.Model):
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.author



