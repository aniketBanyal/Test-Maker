# Generated by Django 3.1.7 on 2021-03-19 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taker', '0003_taker_showanwers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taker',
            old_name='showAnwers',
            new_name='showAnswers',
        ),
    ]
