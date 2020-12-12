# Generated by Django 3.1.4 on 2020-12-06 18:28

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_auto_20201206_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='coordinates',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.TextField(blank=True, verbose_name='Place'),
        ),
    ]