# Generated by Django 2.2.20 on 2021-05-08 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0009_remove_house_uniquenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='UniqueNumber',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
