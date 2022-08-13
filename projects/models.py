from django.db import models
from django.conf import settings


class Project(models.Model):
   title = models.CharField(max_length=200)
   description = models.TextField()
   technology = models.CharField(max_length=200)
   members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="projects",
    )
   image = models.FilePathField(path="static/img")

   def __str__(self):
       return f"{self.title} | {self.technology}"
