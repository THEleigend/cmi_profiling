# Generated by Django 4.0 on 2023-04-13 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consortium', '0017_consortium'),
    ]

    operations = [
        migrations.AddField(
            model_name='cmi',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=100),
        ),
    ]
