from django.db import models


class Loan(models.Model):
    class Meta:
        ordering = ("id",)

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="loans",
    )

    copy = models.ForeignKey(
        "book_copy.Copy",
        on_delete=models.CASCADE,
        related_name="copys",
    )

    return_date = models.DateField(
        null=False,
        auto_now_add=True,
           
    )
