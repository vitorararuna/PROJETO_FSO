# Generated by Django 5.1.1 on 2024-09-16 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_admin_open'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='open',
            field=models.CharField(default='False', max_length=100),
        ),
    ]
