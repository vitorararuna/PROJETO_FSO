# Generated by Django 5.1.1 on 2024-09-16 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_turma_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='turma',
            name='reservas',
            field=models.CharField(default='', max_length=100),
        ),
    ]
