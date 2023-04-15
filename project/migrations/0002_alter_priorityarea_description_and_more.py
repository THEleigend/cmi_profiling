# Generated by Django 4.0 on 2023-03-21 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commodity', '0008_alter_commodity_consortium_name'),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priorityarea',
            name='description',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='proj_type',
            field=models.CharField(choices=[('R&D', 'R&D'), ('Non-R&D', 'Non-R&D')], default='R&D', max_length=20, verbose_name='Project Type'),
        ),
        migrations.AlterField(
            model_name='projectoutput',
            name='iec_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='commodity.iecmaterial'),
        ),
    ]
