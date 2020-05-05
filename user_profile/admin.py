"""
Project    : "CCRH"
module     : User Profile/admin
created    : 03/03/2020
Author     : Manish Kumar
"""

from django.contrib import admin
from user_profile.models import ( Profilestatus,PractDetails,PractCertificateUpload,
                                  AdditionalProfile,EmailTemplate,SmsTemplate,PractClinicalSettings,PractCsDetails
                           )
from django.utils.translation import ugettext, ugettext_lazy as _
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget, DateTimeWidget, IntegerWidget
from import_export.admin import ImportMixin, ExportMixin, ImportExportMixin
from import_export.formats import base_formats
from django.contrib.auth.models import User, Permission, Group
from django.forms import forms, ModelForm, Select
from import_export import resources, fields
from django.contrib.auth.admin import UserAdmin
from master.models import (State,Status,ClinicalSetting)

from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from django.core.mail import send_mail,EmailMultiAlternatives,EmailMessage
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.utils.html import strip_tags, format_html
from django.contrib.auth.forms import (UserCreationForm)
from django.utils.crypto import get_random_string
from django.db.models.functions import Lower
import random
import string




# Register your models here.
class ProfilestatusAdmin(admin.ModelAdmin):
    list_display = ('profile_status',)
    
    
# Profile ADMIN - START 

class AdditionalProfileInline(NestedStackedInline):
    model = AdditionalProfile
    can_delete = False
    verbose_name_plural = _('Additional Profile')
    extra = 1
    max_num = 1
    fk_name = 'user'
    fields = ('mobile_no', 'state', 'city', 'pincode', 'address_line1', 'profile_status',)

class PractCertificateUploadInline(NestedStackedInline):
    model = PractCertificateUpload
    can_delete = False
    verbose_name_plural = _('Upload Registration Certificate')
    extra = 1
    max_num = 1
    fields = ('document_path',)
    fk_name = 'pract'

class PractClinicalSettingsInline(NestedStackedInline):
    model = PractClinicalSettings
    can_delete = False
    verbose_name_plural = _('Type Of Clinical Settings')
    extra = 1
    fields = ('cs',)
    fk_name = 'pract'
    
class PractCsDetailsInline(NestedStackedInline):
    model = PractCsDetails
    can_delete = False
    verbose_name_plural = _('Practitioners Clinical Setting Details')
    extra = 1
    fields = ('clinic_name', 'clinic_address',)
    fk_name = 'pract'
    
class PractDetailsInline(NestedStackedInline):
    model = PractDetails
    can_delete = False
    verbose_name_plural = _('Practitioners Details')
    extra = 1
    max_num = 1
    fk_name = 'user'
    fields = ('pract_regis_body', 'state', 'pract_reg_no', 'affiliation', 'cs_num', 'tnc',)
    inlines = [PractCertificateUploadInline, PractClinicalSettingsInline, PractCsDetailsInline] 


class UserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['groups'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True
        self.fields['password1'].required = False
        self.fields['password2'].required = False
        
        # If one field gets auto completed but not the other, our 'neither
        # password or both password' validation will be triggered.
        self.fields['password1'].widget.attrs['autocomplete'] = 'off'
        self.fields['password2'].widget.attrs['autocomplete'] = 'off'
        
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            user = User.objects.exclude(pk=self.instance.pk).get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError(u'Email %s is already in use.' % email)
    
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.exclude(pk=self.instance.pk).get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(u'Username %s is already in use.' % username)
       
class CustomUserAdmin(UserAdmin, NestedModelAdmin):
    UserAdmin.inlines = list(UserAdmin.inlines)+ [AdditionalProfileInline, PractDetailsInline]
    UserAdmin.list_display = list(UserAdmin.list_display)
    add_form = UserCreationForm
    fieldsets = (
        (
        None,{'fields': ('groups', 'first_name', 'last_name', 'email',  'username', 'is_active', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('groups', 'first_name', 'last_name', 'email',  'username', 'is_active', ),}),
    )
    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

    def __init__(self, *args, **kwargs):
        super(UserAdmin,self).__init__(*args, **kwargs)
        UserAdmin.list_display = list(UserAdmin.list_display)
        UserAdmin.actions = list(UserAdmin.actions)
    
    @receiver(post_save,sender=PractDetails)
    def send_mail_when_user_created_by_admin(sender, instance, **kwargs):
        user_obj = AdditionalProfile.objects.get(user = instance.user)
        print(user_obj,'user_obj')
        if user_obj.profile_status.profile_status.lower() == "approved" and not kwargs['created']:
            random_pass = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(8)])
            if instance.user.password is not None:
                instance.user.set_password(random_pass)
                instance.user.save()
            send_email = EmailTemplate.objects.get(email_code='CCEM001')
            subject = send_email.email_subject
            to_email = instance.user.email
            from_email, to = settings.ADMIN_EMAIL, [to_email]
            html_content = send_email.email_body.format(user_name=instance.user.first_name +' '+ instance.user.last_name,
                                                        email_id = instance.user.email, password = random_pass,
                                                    )
            text_content = format_html(html_content)
            email = EmailMultiAlternatives(subject,
                                            text_content, 
                                            from_email, 
                                            to)
            email.content_subtype = 'html'
            email.send()
            
# Profile ADMIN - END


class EmailTemplateResource(resources.ModelResource):
    email_code = fields.Field(column_name='Email Code', attribute='email_code')
    email_subject = fields.Field(column_name='Email Subject', attribute='email_subject')
    sent_to = fields.Field(column_name='Send To', attribute='sent_to')
    trigger_point = fields.Field(column_name='Trigger Point', attribute='trigger_point')
    
    
    class Meta:
        model = EmailTemplate
        fields = ('sent_to','trigger_point','email_code','email_subject','email_body')
        export_order = fields


class EmailTemplateAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = EmailTemplateResource
    list_display = ('email_code','email_subject','sent_to','trigger_point')
    search_fields = ('email_code','email_subject','sent_to','trigger_point')
    fields = ('email_code','sent_to','trigger_point','email_subject','email_body')
    readonly_fields=('email_code',)
    
    def has_delete_permission(self, request, obj=None):
        return False
    

# Subscription Plan MODEL - END

class SMSTemplateResource(resources.ModelResource):
    sms_code = fields.Field(column_name='SMS Code', attribute='sms_code')
    sms_text = fields.Field(column_name='SMS Text', attribute='sms_text')
    sent_to = fields.Field(column_name='Send To', attribute='sent_to')
    trigger_point = fields.Field(column_name='Trigger Point', attribute='trigger_point')
    
    class Meta:
        model = SmsTemplate
        fields = ('sent_to','trigger_point','sms_code','sms_text')
        export_order = fields


class SmsTemplateAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = SMSTemplateResource
    list_display = ('sms_code','sms_text','sent_to','trigger_point')
    search_fields = ('sms_code','sms_text','sent_to','trigger_point')
    fields = ('sms_code','sent_to','trigger_point','sms_text')
    readonly_fields=('sms_code',)
    
    def has_delete_permission(self, request, obj=None):
        return False
 
 
    
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)    
admin.site.register(EmailTemplate, EmailTemplateAdmin)
admin.site.register(SmsTemplate, SmsTemplateAdmin)
# admin.site.register(Profilestatus, ProfilestatusAdmin)