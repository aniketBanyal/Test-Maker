# Generated by Django 3.1.7 on 2021-03-18 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_auto_20210318_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='timeLimit',
            field=models.TimeField(null=True),
        ),
    ]
