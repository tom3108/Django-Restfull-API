from django.db import models

class Movie (models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    after_prem = models.BooleanField(default=False)
    premiere = models.DateField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    imdb_rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name()

    def name (self):
        return self.title + " (" + str(self.year) + ")"




