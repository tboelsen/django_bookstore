# Generated by Django 3.0.3 on 2020-10-09 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20200923_1657'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='book',
            index=models.Index(fields=['id'], name='id_index'),
        ),
    ]
