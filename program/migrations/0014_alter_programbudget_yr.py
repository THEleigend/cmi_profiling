# Generated by Django 4.0 on 2023-03-21 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0013_remove_researcher_bach_deg_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programbudget',
            name='yr',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
