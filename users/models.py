from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_librarian = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)

    copies = models.ManyToManyField("book_copy.Copy", related_name="Loan")
    books = models.ManyToManyField("books.Book", related_name="readers")

    def __str__(self):
        return self.email
