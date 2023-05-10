from django.db import models


class Copy(models.Model):
    class Meta:
        ordering = ("id",)

    book = models.ForeignKey(
        "books.Book",
        on_delete=models.CASCADE,
        related_name="copys",
    )

    is_rented = models.BooleanField(default=False)
