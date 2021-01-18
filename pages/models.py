from django.db import models

# Create your models here.
class Slider(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=700, blank=False)
    image = models.ImageField(upload_to='slider/', blank=False)

    def __str__(self):
        return self.title

class About(models.Model):
    title = models.CharField(max_length=200, blank=False)
    image = models.ImageField(upload_to='about/', blank=False)
    description = models.TextField(max_length=700, blank=False)

    def __str__(self):
        return self.title
        
class Client(models.Model):
    title = models.CharField(max_length=200, blank=False)
    image = models.ImageField(upload_to='client/', blank=False)
    

    def __str__(self):
        return self.title

class Team(models.Model):
    name = models.CharField(max_length=200, blank=False)
    title = models.CharField(max_length=200, blank=False)
    image = models.ImageField(upload_to='team/', blank=False)
    

    def __str__(self):
        return self.name

class Testimonials(models.Model):
    name = models.CharField(max_length=200, blank=False)
    title = models.CharField(max_length=200, blank=False)
    image = models.ImageField(upload_to='testimonials/', blank=False)
    description = models.TextField(max_length=700, blank=False)

    def __str__(self):
        return self.name
