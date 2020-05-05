# Generated by Django 2.2.11 on 2020-04-14 15:41

import audit_log.models.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import user_profile.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('master', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profilestatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_status', models.CharField(max_length=50, verbose_name='Profile Status')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('created_by', audit_log.models.fields.CreatingUserField(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ProfilestatusCreatedBy', to=settings.AUTH_USER_MODEL)),
                ('updated_by', audit_log.models.fields.LastUserField(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ProfilestatusUpdatedBy', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile status',
                'verbose_name_plural': 'Profile status',
                'db_table': 'ccrh_user_profile_status',
            },
        ),
        migrations.CreateModel(
            name='AdditionalProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_no', models.BigIntegerField(verbose_name='Mobile Number ')),
                ('addt_mobile_no', models.BigIntegerField(blank=True, null=True, verbose_name='Additional Mobile Number ')),
                ('photo', models.ImageField(blank=True, default='', null=True, upload_to='Profile_image/', verbose_name='Profile Photo')),
                ('address_line1', models.TextField(blank=True, null=True, verbose_name='Address Line1')),
                ('address_line2', models.TextField(blank=True, null=True, verbose_name='Address Line2')),
                ('pincode', models.BigIntegerField(blank=True, null=True, verbose_name='Pincode')),
                ('profile_approved_datetime', models.DateTimeField(blank=True, null=True, verbose_name=' Profile Approved Date Time')),
                ('profile_approved_remarks', models.TextField(blank=True, null=True, verbose_name='Profile Approved Remarks')),
                ('profile_dis_opt_by_remarks', models.TextField(blank=True, null=True, verbose_name='Profile Dis Opt By Remarks')),
                ('profile_dis_opt_by_datetime', models.DateTimeField(blank=True, null=True, verbose_name=' Profile Dis Opt By Datetime')),
                ('profile_dis_by_remarks', models.TextField(blank=True, null=True, verbose_name='Profile Disease By Remarks')),
                ('profile_dis_by_datetime', models.DateTimeField(blank=True, null=True, verbose_name=' Profile Dis By Datetime')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.City', verbose_name='City Id')),
                ('created_by', audit_log.models.fields.CreatingUserField(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='AdditionalProfileCreatedBy', to=settings.AUTH_USER_MODEL)),
                ('profile_approved_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ProfileApprovedBy', to=settings.AUTH_USER_MODEL, verbose_name='Profile Approved By')),
                ('profile_dis_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ProfiledisBy', to=settings.AUTH_USER_MODEL, verbose_name='Profile Dis By')),
                ('profile_status', models.ForeignKey(default=user_profile.models.get_profile_status, on_delete=django.db.models.deletion.CASCADE, to='user_profile.Profilestatus', verbose_name=' Profile status')),
                ('state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.State', verbose_name='State Id')),
                ('updated_by', audit_log.models.fields.LastUserField(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='AdditionalProfileUpdatedBy', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User Id')),
            ],
            options={
                'verbose_name': 'Additional Profile',
                'verbose_name_plural': 'Additional Profile',
                'db_table': 'ccrh_user_additional_profile',
            },
        ),
    ]
