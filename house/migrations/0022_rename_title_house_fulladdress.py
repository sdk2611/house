# Generated by Django 3.2.2 on 2021-05-10 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0021_house_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='house',
            old_name='title',
            new_name='fullAddress',
        ),
    ]
