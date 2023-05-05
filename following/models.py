from django.db import models


class Follow(models.Model):
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="user_following_books"
    )

    book = models.ForeignKey(
        "books.Book", on_delete=models.CASCADE, related_name="following_books"
    )
