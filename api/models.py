from django.db import models

class Movie (models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    after_prem = models.BooleanField(default=False)


