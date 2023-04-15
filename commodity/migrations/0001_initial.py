# Generated by Django 4.0 on 2023-03-08 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth_user', '0001_initial'),
        ('consortium', '0008_alter_consortium_modified_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='IecMaterial',
            fields=[
                ('iec_id', models.AutoField(primary_key=True, serialize=False)),
                ('iec_type', models.CharField(blank=True, max_length=100, null=True)),
                ('title', models.CharField(max_length=255)),
                ('target_audience', models.CharField(blank=True, max_length=100, null=True)),
                ('designed_by', models.CharField(blank=True, max_length=100, null=True)),
                ('content_by', models.CharField(blank=True, max_length=100, null=True)),
                ('date_published', models.DateField(blank=True, null=True)),
                ('ip', models.CharField(blank=True, max_length=30, null=True)),
                ('iec_file', models.FileField(blank=True, null=True, upload_to='iec_files/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='auth_user.user')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='auth_user.user')),
            ],
            options={
                'db_table': 'iecmaterial',
            },
        ),
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('com_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('detail', models.TextField(blank=True, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='com_img/')),
                ('produced_by', models.TextField(blank=True, null=True)),
                ('geolat', models.FloatField(blank=True, null=True)),
                ('geolong', models.FloatField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('consortium_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='consortium.consortium')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='auth_user.user')),
                ('iec_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='commodity.iecmaterial')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='auth_user.user')),
            ],
            options={
                'db_table': 'commodity',
            },
        ),
    ]
