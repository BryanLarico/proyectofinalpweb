# Generated by Django 5.0.6 on 2024-06-11 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_course_options_course_hourspractice_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={},
        ),
        migrations.RemoveConstraint(
            model_name='course',
            name='unique_nameCourse',
        ),
    ]
