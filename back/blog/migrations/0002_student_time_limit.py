# Generated by Django 5.1.1 on 2024-09-04 16:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='time_limit',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
