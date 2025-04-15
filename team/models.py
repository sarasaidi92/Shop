from django.db import models

class Team(models.Model):
    text = models.TextField(max_length=100, blank=True)
    name = models.CharField(max_length=100, blank=True)
    job = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

