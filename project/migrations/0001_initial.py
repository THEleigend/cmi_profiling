# Generated by Django 4.0 on 2023-03-16 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('consortium', '0010_alter_consortium_consortium_logo'),
        ('auth_user', '0001_initial'),
        ('commodity', '0004_alter_commodity_consortium_name'),
        ('program', '0012_alter_program_consortium'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriorityArea',
            fields=[
                ('priority_id', models.AutoField(primary_key=True, serialize=False)),
                ('area', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='auth_user.user')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='auth_user.user')),
            ],
            options={
                'db_table': 'priority_area',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('proj_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('proj_description', models.TextField(blank=True, null=True)),
                ('proj_type', models.CharField(choices=[('R&D', 'R&D'), ('Non-R&D', 'Non-R&D')], default='R&D', max_length=20)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('final_impl_date', models.DateField(blank=True, null=True)),
                ('duration', models.CharField(max_length=100)),
                ('approved_budget', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('approved_date', models.DateField(blank=True, null=True)),
                ('daterequestedext', models.DateField(blank=True, null=True)),
                ('ext_duration', models.IntegerField(blank=True, null=True)),
                ('proj_file', models.FileField(blank=True, null=True, upload_to='project_files/')),
                ('date_uploaded', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('ongoing', 'ongoing'), ('finished', 'finished')], default='ongoing', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('co_impl_agency', models.ManyToManyField(blank=True, related_name='co_impl_agency', to='program.Agency')),
                ('commodity', models.ManyToManyField(blank=True, to='commodity.Commodity')),
                ('consortium', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='consortium.consortium')),
                ('coop_agency', models.ManyToManyField(blank=True, related_name='coop_agency', to='program.Agency')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='auth_user.user')),
                ('fund_agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='program.agency')),
                ('impl_agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='program.agency')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='auth_user.user')),
                ('priority', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='project.priorityarea')),
                ('prog_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='program.program')),
                ('proj_leader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='program.researcher')),
                ('proj_stakeholder', models.ManyToManyField(blank=True, to='program.Stakeholder')),
                ('proj_team', models.ManyToManyField(blank=True, to='program.Researcher')),
                ('requested_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='program.researcher')),
            ],
            options={
                'db_table': 'project',
            },
        ),
        migrations.CreateModel(
            name='Sdg',
            fields=[
                ('sdg_no', models.AutoField(primary_key=True, serialize=False)),
                ('sdg_title', models.CharField(max_length=100)),
                ('sdg_desc', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='auth_user.user')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='auth_user.user')),
            ],
            options={
                'db_table': 'sdg',
            },
        ),
        migrations.CreateModel(
            name='ProjectOutput',
            fields=[
                ('projout_id', models.AutoField(primary_key=True, serialize=False)),
                ('proj_output_type', models.CharField(choices=[('Publication', 'Publication'), ('Patent', 'Patent'), ('Property', 'Property'), ('Product', 'Product'), ('People', 'People'), ('Place and Partnership', 'Place and Partnership')], default='Publication', max_length=100)),
                ('proj_output_desc', models.TextField(blank=True, null=True)),
                ('iec_id', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='auth_user.user')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='auth_user.user')),
                ('proj_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='project.project')),
            ],
            options={
                'db_table': 'proj_output',
            },
        ),
        migrations.CreateModel(
            name='ProjectImplementingSite',
            fields=[
                ('projimp', models.AutoField(primary_key=True, serialize=False)),
                ('barangay', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('province', models.CharField(blank=True, max_length=100, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=5, null=True)),
                ('geolat', models.FloatField(blank=True, null=True)),
                ('geolong', models.FloatField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='auth_user.user')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='auth_user.user')),
                ('proj_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='project.project')),
            ],
            options={
                'db_table': 'proj_imp_site',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='sdg_no',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='project.sdg'),
        ),
    ]
