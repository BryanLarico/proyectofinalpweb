# Generated by Django 5.0.6 on 2024-06-11 21:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_course_options_remove_course_unique_namecourse'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='course',
            name='credit',
            field=models.IntegerField(null=True),
        ),
    ]
