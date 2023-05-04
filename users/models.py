from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_librarian = models.BooleanField(default=False)
    # copies = models.ManyToManyField("Copy", related_name="Loan")
    books = models.ManyToManyField("books.Book", related_name="followers")

    def __str__(self):
        return self.email
