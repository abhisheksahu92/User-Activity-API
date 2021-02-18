# Generated by Django 3.1.6 on 2021-02-17 15:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserActivity', '0003_auto_20210216_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(max_length=7, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 7', regex='^.{7}$')]),
        ),
    ]
