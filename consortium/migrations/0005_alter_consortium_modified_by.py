# Generated by Django 4.0 on 2023-03-07 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_user', '0001_initial'),
        ('consortium', '0004_alter_consortium_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consortium',
            name='modified_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='auth_user.user'),
        ),
    ]
