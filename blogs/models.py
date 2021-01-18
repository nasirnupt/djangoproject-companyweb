from django.db import models
from datetime import datetime

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=300, blank=False)
    name = models.CharField(max_length=100, blank=False)
    publish_date = models.DateTimeField(default=datetime.now, blank=False)
    comment = models.IntegerField()
    description = models.TextField(max_length=700, blank=True)
    image = models.ImageField(upload_to='blog/', blank=False)

    def __str__(self):
        return self.name

class recentpost(models.Model):
    image = models.ImageField(blank=False)
    title = models.CharField(max_length=200, blank=False)
    publish_date = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return self.title
