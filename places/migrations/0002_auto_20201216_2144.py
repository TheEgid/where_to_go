# Generated by Django 3.1.4 on 2020-12-16 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='placeId',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]