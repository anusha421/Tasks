# Generated by Django 4.0.1 on 2022-07-14 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0002_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='body',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]
