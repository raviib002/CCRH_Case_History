from django.db import models
from django.utils.translation import ugettext_lazy as _
from audit_log.models.fields import CreatingUserField, LastUserField
from django.contrib.auth.models import User, Group
from django.db.models.deletion import CASCADE
from random import choices
from master.models import (State,City,Status,ClinicalSetting)
from ckeditor.fields import RichTextField

#Creating model for Status Table Starts here
class Profilestatus(models.Model):
    profile_status = models.CharField(max_length=50, verbose_name=_("Profile Status"))
    created_by = CreatingUserField(related_name = "ProfilestatusCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "ProfilestatusUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.profile_status
    
    class Meta:
        verbose_name = "Profile status"
        verbose_name_plural = "Profile status"
        db_table = 'ccrh_user_profile_status'
        
#Default keeping the profile status 1
def get_profile_status():
    return Profilestatus.objects.get(profile_status="Pending for Approval")
        
#Creating model for Additional Profile Table Starts here
class AdditionalProfile(models.Model):
    Profile_dis_CHOICE = ( 
        (u'0', u'No'),
        (u'1', u'Opt for Disable'),
        )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User"))
    mobile_no = models.BigIntegerField( verbose_name=_("Mobile Number "), unique=True)
    addt_mobile_no = models.BigIntegerField(blank=True, null=True, verbose_name=_("Additional Mobile Number "))
    photo = models.ImageField(upload_to='Profile_image/', default='', blank=True, null=True, verbose_name="Profile Photo")
    address_line1 = models.TextField(blank=True, null=True,verbose_name=_("Address Line1")) 
    address_line2 = models.TextField(blank=True, null=True,verbose_name=_("Address Line2"))
    state =  models.ForeignKey(State, blank=True, null=True, on_delete=models.CASCADE, verbose_name=_("State"))
    city =  models.ForeignKey(City,  blank=True, null=True, on_delete=models.CASCADE, verbose_name=_("City"))
    pincode = models.BigIntegerField(blank=True, null=True,  verbose_name=_("Pincode"))
    profile_status = models.ForeignKey(Profilestatus, default=get_profile_status,on_delete=models.CASCADE, verbose_name=_(" Profile status"))
    profile_approved_by =  models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, verbose_name=_("Profile Approved By"), related_name = "ProfileApprovedBy")
    profile_approved_datetime = models.DateTimeField(verbose_name=(" Profile Approved Date Time"), blank=True, null=True)
    profile_approved_remarks = models.TextField(blank=True, null=True,verbose_name=_("Profile Approved Remarks")) 
    profile_dis_opt_by_status = models.CharField(max_length=1, default='0',choices=Profile_dis_CHOICE, verbose_name=_("Prfile Dis Opt By Status"))
    profile_dis_opt_by_remarks =  models.TextField(blank=True, null=True,verbose_name=_("Profile Dis Opt By Remarks")) 
    profile_dis_opt_by_datetime = models.DateTimeField(verbose_name=(" Profile Dis Opt By Datetime"), blank=True, null=True)
    profile_dis_by= models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, verbose_name=_("Profile Dis By"), related_name = "ProfiledisBy")
    profile_dis_by_remarks = models.TextField(blank=True, null=True,verbose_name=_("Profile Disease By Remarks")) 
    profile_dis_by_datetime =  models.DateTimeField(verbose_name=(" Profile Dis By Datetime"), blank=True, null=True)
    created_by = CreatingUserField(related_name = "AdditionalProfileCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "AdditionalProfileUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    class Meta:
        verbose_name = "Additional Profile"
        verbose_name_plural = "Additional Profile"
        db_table = 'ccrh_user_additional_profile'

#Creating model for  Practical Details Table Starts here
class PractDetails(models.Model):
    BODY_CHOICE = (
        (u'1', u'CCH'),
        (u'2', u'STATE'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User"))
    pract_regis_body = models.CharField(max_length=1, choices=BODY_CHOICE, verbose_name=_("Registration Body"))
    state =  models.ForeignKey(State, blank=True, null=True, on_delete=models.CASCADE, verbose_name=_("State"))
    cs_num =  models.IntegerField(verbose_name=_("Clicical Settings"))
    affiliation = models.CharField(max_length=100, verbose_name=_("Affiliation"))
    tnc = models.BooleanField(default=False, verbose_name=_("Terms And Conditions"))
    pract_reg_no =  models.CharField(max_length=50, verbose_name=_("Registration Number"))
#     status =  models.ForeignKey(Status,  on_delete=models.CASCADE, verbose_name=_("Status"))
    created_by = CreatingUserField(related_name = "PractDetailsCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "PractDetailsUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    class Meta:
        verbose_name = "Pract Details"
        verbose_name_plural = "Pract Details"
        db_table = 'ccrh_pract_details'
    
def document_path_name(instance, filename):
    dir_name = instance.pract.user.username 
    return 'Certification Upload/%s/%s' % (dir_name,filename)
    
#Creating model for  Practical Certificate Upload Table Starts here
class PractCertificateUpload(models.Model):
    pract = models.ForeignKey(PractDetails, on_delete=models.CASCADE, verbose_name=_("Pract"))
    document_name = models.CharField(max_length=100, verbose_name=_("Document Name"))
    document_path = models.FileField(blank=True, null=True, upload_to=document_path_name)
    created_by = CreatingUserField(related_name = "PractCertificateUploadCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "PractCertificateUploadUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = "Pract Certificate Upload"
        verbose_name_plural = "Pract Certificate Upload"
        db_table = 'ccrh_pract_cert_upload'

#creating Model for visitor history starts here
class VisitorHistory(models.Model):
    IS_ACCESSED_CHOICE = (
        (u'0', u'No'),
        (u'1', u'Yes'),
    )
    visitor_name = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Visitor Name"))
    visitor_email = models.CharField(max_length=100, verbose_name=_("Visitor Email"))
    visitor_mobile = models.BigIntegerField(verbose_name=_("Visitor Mobile Number ")) 
    visitor_datetime = models.DateTimeField( verbose_name=_("Visitor Date Time"))
    visitor_link_unique_code = models.CharField(max_length=100, verbose_name=_("Visitor Link Unique Code"))
    visitor_link_expiry_datetime = models.DateTimeField( verbose_name=_("Visitor Link Expiry Date Time"))
    is_accessed = models.CharField(max_length=1, default='0',choices=IS_ACCESSED_CHOICE, verbose_name=_("Is Accessed"))
    accessed_datetime = models.DateTimeField( verbose_name=_("Accessed Date Time"))
    created_by = CreatingUserField(related_name = "VisitorHistoryUploadCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "VisitorHistoryUploadUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    class Meta:
        verbose_name = "Visitor History"
        verbose_name_plural = "Visitor History"
        db_table = 'ccrh_vistor_history'
        
        
class EmailTemplate(models.Model):
    email_code = models.CharField(max_length=10, verbose_name=_("Email Code"))
    email_subject = models.TextField(verbose_name=_("Email Subject"))
    email_body = RichTextField(verbose_name=_("Email Body"), help_text=_("Note : Do not change the text inside curly braces {}"))
    sent_to = models.CharField(blank=True, null=True, max_length=200, verbose_name=_("Send To"))
    trigger_point = models.TextField(blank=True, null=True, verbose_name=_("Trigger Point"))
    created_by = CreatingUserField(related_name = "EmailTemplateCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "EmailTemplateUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.email_code
    
    class Meta:
        verbose_name_plural = "Email Template"
        db_table = 'ccrh_email_template'


class SmsTemplate(models.Model):
    sms_code = models.CharField(max_length=10, verbose_name=_("SMS Code"))
    sms_text = models.TextField(verbose_name=_("SMS Text"), help_text=_("Note : Do not change the text inside curly braces {}"))
    trigger_point = models.TextField(blank=True, null=True, verbose_name=_("Trigger Point"))
    sent_to = models.CharField(blank=True, null=True, max_length=200, verbose_name=_("Send To"))
    created_by = CreatingUserField(related_name = "SmsTemplateCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "SmsTemplateUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.sms_code
    
    class Meta:
        verbose_name_plural = "SMS Template"
        db_table = 'ccrh_sms_template'
        
    

#Creating model for  Practical Clinical Settings Details Table Starts here
class PractClinicalSettings(models.Model):
    pract = models.ForeignKey(PractDetails, on_delete=models.CASCADE, verbose_name=_("Pract Details"))
    cs =  models.ForeignKey(ClinicalSetting, on_delete=models.CASCADE, verbose_name=_("Type Of Clinical Setting"))
    created_by = CreatingUserField(related_name = "PractClinicalSettingsCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "PractClinicalSettingsUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    class Meta:
        verbose_name = "Pract Clicnical Settings"
        verbose_name_plural = "Pract Clicnical Settings"
        db_table = 'ccrh_pract_clinical_setting'
        
        
#Creating model for  Practical Details Table Starts here
class PractCsDetails(models.Model):
    pract = models.ForeignKey(PractDetails, on_delete=models.CASCADE, verbose_name=_("Practical Details"))
    clinic_name = models.CharField(max_length=100, verbose_name=_("Clinical Name"))
    clinic_address = models.TextField(verbose_name=_("Clinical Address"))
    created_by = CreatingUserField(related_name = "PractCsDetailsCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "PractCsDetailsUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    class Meta:
        verbose_name = "Pract Clinical Setting Details"
        verbose_name_plural = "Pract Clinical Setting Details"
        db_table = 'ccrh_pract_cs_detail'