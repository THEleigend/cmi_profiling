# Generated by Django 4.0 on 2023-04-12 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0012_alter_team_mname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='teams',
            field=models.CharField(max_length=60),
        ),
    ]
