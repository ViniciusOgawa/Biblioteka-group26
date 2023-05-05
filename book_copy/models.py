from django.db import models


class Copy(models.Model):
    class Meta:
        ordering = ("id",)

    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)

    book = models.ForeignKey(
        "books.Book",
        on_delete=models.CASCADE,
        related_name="copys",
    )
