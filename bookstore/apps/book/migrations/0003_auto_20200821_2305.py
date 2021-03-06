# Generated by Django 3.1 on 2020-08-22 02:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_remove_client_borrowed_books'),
        ('book', '0002_book_borrowed_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='borrowed_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='borrowed_books', to='client.client'),
        ),
    ]
