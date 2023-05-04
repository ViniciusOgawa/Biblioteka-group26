from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)

    users = models.ManyToManyField("users.Users", related_name="books_following")
