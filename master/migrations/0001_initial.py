# Generated by Django 2.2.11 on 2020-04-14 15:41

import audit_log.models.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=200, verbose_name='Status')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('created_by', audit_log.models.fields.CreatingUserField(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='StatusCreatedBy', to=settings.AUTH_USER_MODEL)),
                ('updated_by', audit_log.models.fields.LastUserField(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='StatusUpdatedBy', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Status',
                'verbose_name_plural': 'Status',
                'db_table': 'ccrh_master_status',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=100, verbose_name='State Name')),
                ('country_id', models.CharField(choices=[('1', 'INDIA')], default=1, max_length=1, verbose_name='Country Name')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('created_by', audit_log.models.fields.CreatingUserField(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='StateCreatedBy', to=settings.AUTH_USER_MODEL)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.Status', verbose_name='Status')),
                ('updated_by', audit_log.models.fields.LastUserField(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='StateUpdatedBy', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'State',
                'verbose_name_plural': 'State',
                'db_table': 'ccrh_master_state',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=100, verbose_name='City Name')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('created_by', audit_log.models.fields.CreatingUserField(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='CityCreatedBy', to=settings.AUTH_USER_MODEL)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.State', verbose_name='State Name')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.Status', verbose_name='Status')),
                ('updated_by', audit_log.models.fields.LastUserField(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='CityUpdatedBy', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'City',
                'db_table': 'ccrh_master_city',
            },
        ),
    ]
