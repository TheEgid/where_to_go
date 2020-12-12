# Generated by Django 3.1.4 on 2020-12-07 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_auto_20201206_2128'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='place',
            options={'ordering': ['title', 'placeId']},
        ),
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.TextField(blank=True, max_length=200, verbose_name='Place'),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='img', max_length=200, verbose_name='Image')),
                ('image', models.ImageField()),
                ('location', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='places.place')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]