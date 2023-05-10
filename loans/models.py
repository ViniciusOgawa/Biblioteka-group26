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

    returned = models.BooleanField(default=False)

    loan_date = models.DateField(auto_now_add=True)

    return_date = models.DateField(null=True, blank=True)
