# Generated by Django 5.2 on 2025-04-13 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobopportunities', '0002_jobpost_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='deadline',
            field=models.DateField(blank=True, null=True),
        ),
    ]
