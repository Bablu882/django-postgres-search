# Generated by Django 4.1.4 on 2022-12-19 04:14

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_remove_book_author_book_authors'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='book',
            index=django.contrib.postgres.indexes.GinIndex(fields=['title'], name='NewGinIndex', opclasses=['gin_trgm_ops']),
        ),
    ]
