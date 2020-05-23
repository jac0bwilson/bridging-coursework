from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Education(models.Model):
    ed_type = models.CharField(max_length=200)
    more_detail = models.CharField(max_length=200)
    content = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.ed_type

class Skill(models.Model):
    technical = models.BooleanField()
    content = models.CharField(max_length=100)

    def publish(self):
        self.save()

    def __str__(self):
        return self.content

class Experience(models.Model):
    exp_type = models.CharField(max_length=200)
    more_detail = models.CharField(max_length=200)
    content = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.exp_type