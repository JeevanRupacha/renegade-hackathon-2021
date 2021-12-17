# Generated by Django 3.2.9 on 2021-12-17 07:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20211217_1250'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('relationship', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=25)),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in +977 format.', regex='^\\+?1?\\d{9,15}$')])),
            ],
            options={
                'verbose_name_plural': 'location',
            },
        ),
    ]
