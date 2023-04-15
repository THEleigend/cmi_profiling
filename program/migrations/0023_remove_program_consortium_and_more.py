# Generated by Django 4.0 on 2023-04-13 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consortium', '0013_cmi_remove_consortium_created_by_and_more'),
        ('program', '0022_alter_programbudget_eo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='consortium',
        ),
        migrations.RemoveField(
            model_name='stakeholder',
            name='consortium_id',
        ),
        migrations.AddField(
            model_name='stakeholder',
            name='cmi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='consortium.cmi'),
        ),
        migrations.AlterField(
            model_name='program',
            name='co_impl_agency',
            field=models.ManyToManyField(blank=True, to='consortium.CMI'),
        ),
        migrations.AlterField(
            model_name='program',
            name='funding_agency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='consortium.cmi'),
        ),
        migrations.AlterField(
            model_name='program',
            name='impl_agency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='consortium.cmi'),
        ),
        migrations.AlterField(
            model_name='programbudget',
            name='fund_source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='consortium.cmi'),
        ),
        migrations.AlterField(
            model_name='researcher',
            name='cmi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='consortium.cmi'),
        ),
    ]
