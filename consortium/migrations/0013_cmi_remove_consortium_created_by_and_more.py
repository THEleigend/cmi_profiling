# Generated by Django 4.0 on 2023-04-13 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consortium', '0012_alter_consortium_fb_url_alter_consortium_url_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CMI',
            fields=[
                ('agency_id', models.AutoField(primary_key=True, serialize=False)),
                ('agency_code', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=255)),
                ('is_cmi', models.BooleanField(default=False)),
                ('address', models.CharField(max_length=255)),
                ('geolat', models.FloatField(blank=True, null=True)),
                ('geolong', models.FloatField(blank=True, null=True)),
                ('contact_no', models.CharField(max_length=40)),
                ('logo', models.ImageField(upload_to='cmi_logos/')),
                ('detail', models.TextField(blank=True, null=True)),
                ('telno', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('url', models.URLField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'cmi',
            },
        ),
        migrations.RemoveField(
            model_name='consortium',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='consortium',
            name='modified_by',
        ),
    ]
