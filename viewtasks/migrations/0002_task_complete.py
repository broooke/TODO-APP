# Generated by Django 3.1.3 on 2020-12-12 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewtasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
