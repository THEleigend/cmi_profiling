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
            name='Secretariat',
            fields=[
                ('secretariat_id', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('mname', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('email_add', models.CharField(max_length=100)),
                ('contact_no', models.CharField(max_length=20)),
                ('dob', models.DateField(blank=True, null=True)),
                ('sex', models.CharField(max_length=10)),
                ('bach_deg', models.CharField(blank=True, max_length=100, null=True)),
                ('bdyearcompleted', models.IntegerField(blank=True, null=True)),
                ('mas_deg', models.CharField(blank=True, max_length=100, null=True)),
                ('mdyearcompleted', models.IntegerField(blank=True, null=True)),
                ('doc_deg', models.CharField(blank=True, max_length=100, null=True)),
                ('ddyearcompleted', models.IntegerField(blank=True, null=True)),
                ('specialization', models.CharField(blank=True, max_length=255, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='secretariat_photo/')),
                ('pds_file', models.FileField(blank=True, null=True, upload_to='secretariat_pds/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('consortium', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='consortium.consortium')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='auth_user.user')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='auth_user.user')),
            ],
            options={
                'db_table': 'secretariat',
            },
        ),
    ]
