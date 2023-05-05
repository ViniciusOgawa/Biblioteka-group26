# Generated by Django 4.2.1 on 2023-05-05 16:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("book_copy", "0001_initial"),
        ("books", "0002_book_author_book_name"),
        ("users", "0003_user_is_blocked"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="books",
            field=models.ManyToManyField(related_name="readers", to="books.book"),
        ),
        migrations.AddField(
            model_name="user",
            name="copies",
            field=models.ManyToManyField(related_name="Loan", to="book_copy.copy"),
        ),
    ]
