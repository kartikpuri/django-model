# Generated by Django 3.1 on 2020-08-13 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='book_shelf',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.bookshelf'),
        ),
    ]
