# Generated by Django 3.1.6 on 2021-02-12 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='place',
            options={'ordering': ['title', 'id']},
        ),
        migrations.RenameField(
            model_name='place',
            old_name='placeId',
            new_name='id',
        ),
    ]
