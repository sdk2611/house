# Generated by Django 2.2.20 on 2021-05-08 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0007_auto_20210508_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='UniqueNumber',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='livingroom',
            name='UniqueNumber',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='residentialpremises',
            name='UniqueNumber',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]