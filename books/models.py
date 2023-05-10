from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=50, default=None)
    author = models.CharField(max_length=50, default=None)

    users = models.ManyToManyField("users.User", related_name="books_following")
