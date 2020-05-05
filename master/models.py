from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User, Group
from audit_log.models.fields import CreatingUserField, LastUserField
from django.db.models.deletion import CASCADE
from random import choices
from django.core.validators import MinLengthValidator
from django.core.validators import MaxLengthValidator


# Create your models here.      
class Status(models.Model):
    status_name = models.CharField(verbose_name=_("Status"), max_length=50)
    created_by = CreatingUserField(related_name = "StatusCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "StatusUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.status_name
     
    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Status"
        db_table = 'ccrh_master_status'
        
#Creating model for state Table Starts here
class State(models.Model):
    COUNTRY_CHOICES = (
        (u'1', u'INDIA'),
    )
    state_name = models.CharField(max_length=100, verbose_name=_("State Name"))
    country_id = models.CharField(max_length=1,default=1, choices=COUNTRY_CHOICES, verbose_name=_("Country Name"))
    status =  models.ForeignKey(Status,  on_delete=models.CASCADE, verbose_name=_("Status"))
    created_by = CreatingUserField(related_name = "StateCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "StateUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.state_name
    
    class Meta:
        verbose_name = "State"
        verbose_name_plural = "State"
        db_table = 'ccrh_master_state'
        
#Creating model for city Table Starts here
class City(models.Model):
    city_name = models.CharField(max_length=100, verbose_name=_("City Name"))
    state =  models.ForeignKey(State,  on_delete=models.CASCADE, verbose_name=_("State Name"))
    status =  models.ForeignKey(Status,  on_delete=models.CASCADE, verbose_name=_("Status"))
    created_by = CreatingUserField(related_name = "CityCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "CityUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.city_name
    
    class Meta:
        verbose_name = "City"
        verbose_name_plural = "City"
        db_table = 'ccrh_master_city'
        

#clinical setting creating an table here
class ClinicalSetting(models.Model):
    cs_name = models.CharField(max_length=100, verbose_name=_("Clinical Setting Name"))
    status =  models.ForeignKey(Status,  on_delete=models.CASCADE, verbose_name=_("Status"))      
    created_by = CreatingUserField(related_name = "ClinicalSettingCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "ClinicalSettingUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.cs_name
    
    class Meta:
        verbose_name = "Clinical Setting"
        verbose_name_plural = "Clinical Setting"
        db_table = 'ccrh_pract_clinical_setting_master'
        
#Medicine Type Creating models  starts here    
class MedicineType(models.Model):
    med_type = models.CharField(max_length=100, verbose_name=_("Medicine Type"))
    status =  models.ForeignKey(Status,  on_delete=models.CASCADE, verbose_name=_("Status"))
    created_by = CreatingUserField(related_name = "MedicineTypeCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "MedicineTypeUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.med_type
    
    class Meta:
        verbose_name = "Medicine Type "
        verbose_name_plural = "Medicine Type"
        db_table = 'ccrh_medicine_type'

#Medicine Master  Creating table starts here
class MedicineMaster(models.Model):
    MOTHER_TINCTURE_CHOICES = (
        (u'0', u'No'),
        (u'1', u'Yes'),
    )
    Potency_3x6x_CHOICES = (
        (u'0', u'No'),
        (u'1', u'Yes'),
    )
    Potency_6_CHOICES = (
        (u'0', u'No'),
        (u'1', u'Yes'),
    )
    Potency_30_CHOICES = (
        (u'0', u'No'),
        (u'1', u'Yes'),
    )
    Potency_200_CHOICES = (
        (u'0', u'No'),
        (u'1', u'Yes'),
    )
    Potency_1m_CHOICES = (
        (u'0', u'No'),
        (u'1', u'Yes'),
    )
    med_name = models.CharField(max_length=100, verbose_name=_("Medicine Name"))
    med_type = models.ForeignKey(MedicineType,  on_delete=models.CASCADE, verbose_name=_("Medicine Type"))
    mother_tincture = models.CharField(max_length=1,default=0, choices=MOTHER_TINCTURE_CHOICES, verbose_name=_("Mother Tincture"))
    potency_3x6x =  models.CharField(max_length=1,default=0, choices=Potency_3x6x_CHOICES, verbose_name=_("Potency 3x6x"))
    potency_6 =  models.CharField(max_length=1,default=0, choices=Potency_6_CHOICES, verbose_name=_("Potency 6"))
    potency_30 = models.CharField(max_length=1,default=0, choices=Potency_30_CHOICES, verbose_name=_("Potency 30"))
    potency_200 = models.CharField(max_length=1,default=0, choices=Potency_200_CHOICES, verbose_name=_("Potency 200"))
    potency_1m = models.CharField(max_length=1,default=0, choices=Potency_1m_CHOICES, verbose_name=_("Potency 1m"))
    status =  models.ForeignKey(Status,  on_delete=models.CASCADE, verbose_name=_("Status"))
    created_by = CreatingUserField(related_name = "MedicineMasterCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "MedicineMasterUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.med_name
    
    class Meta:
        verbose_name = "Medicine Master "
        verbose_name_plural = "Medicine Master"
        db_table = 'ccrh_medicine_master'
        
#Symptoms Creating table starts here    
class SymptomsMaster(models.Model):
    sym_name = models.TextField(verbose_name=_("Symptoms Name"))
    sym_desc = models.TextField( verbose_name=_("Symptoms Description"))
    status =  models.ForeignKey(Status,  on_delete=models.CASCADE, verbose_name=_("Status"))
    created_by = CreatingUserField(related_name = "SymptomsMasterCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "SymptomsMasterUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.sym_name
    
    class Meta:
        verbose_name = "Symptoms Master "
        verbose_name_plural = "Symptoms Master"
        db_table = 'ccrh_symptoms_master'
        
#Disease Creating table starts here    
class DiseaseMaster(models.Model):
    dis_name = models.CharField(max_length=150, verbose_name=_("Disease Name"))
    dis_desc = models.TextField( verbose_name=_("Disease Description"))
    dis_icd_code = models.CharField(max_length=15, verbose_name=_("Disease Icd Code"), unique=True)
    status =  models.ForeignKey(Status,  on_delete=models.CASCADE, verbose_name=_("Status"))
    created_by = CreatingUserField(related_name = "DiseaseMasterCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "DiseaseMasterUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.dis_name
    
    class Meta:
        verbose_name = "Disease Master "
        verbose_name_plural = "Disease Master"
        db_table = 'ccrh_disease_master'
        
#Investigation Creating table starts here    
class InvestigationsMaster(models.Model):
    investg_name = models.CharField(max_length=150, verbose_name=_("Investigation Name"), unique=True)
    investg_desc = models.TextField( verbose_name="Investigation Description")
    status =  models.ForeignKey(Status,  on_delete=models.CASCADE, verbose_name=_("Status"))
    created_by = CreatingUserField(related_name = "InvestigationsMasterCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "InvestigationsMasterUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.investg_name
    
    class Meta:
        verbose_name = "Investigation Master "
        verbose_name_plural = "Investigation Master"
        db_table = 'ccrh_investigation_master'

#Habit Creating table starts here    
class HabitMaster(models.Model):
    HABIT_CHOICES = (
        (u'1', u'habits'),
        (u'2', u'diet'),
        (u'3', u'others'),
    )

    hab_name = models.CharField(max_length=100, verbose_name=_("Habit Name"))
    hab_type = models.CharField(max_length=1,choices=HABIT_CHOICES, verbose_name=_("Habit Type"))
    status =  models.ForeignKey(Status,  on_delete=models.CASCADE, verbose_name=_("Status"))
    created_by = CreatingUserField(related_name = "HabitMasterCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "HabitMasterUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.hab_name
    
    class Meta:
        verbose_name = "Habit Master "
        verbose_name_plural = "Habit Master"
        db_table = 'ccrh_habits_master'

#Physcial General Type Creating table starts here    
class PhysicalGeneralType(models.Model):
    gen_type_name = models.CharField(max_length=100, verbose_name=_("General Type Name"))
    status =  models.ForeignKey(Status,  on_delete=models.CASCADE, verbose_name=_("Status"))
    created_by = CreatingUserField(related_name = "PhysicalGeneralTypeCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "PhysicalGeneralTypeUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.gen_type_name 
    
    class Meta:
        verbose_name = "Physical General Type "
        verbose_name_plural = "Physical General Type"
        db_table = 'ccrh_phy_general_type'
        
#Physical General Master Creating table starts here    
class PhysicalGeneralMaster(models.Model):
    Genearl_Type_CHOICES = (
        (u'1', u'Dropdown'),
        (u'2', u'TEXT'),
    )
    gen_type = models.ForeignKey(PhysicalGeneralType,  on_delete=models.CASCADE, verbose_name=_("General Type"))
    gen_name = models.CharField(max_length=100, verbose_name=_("General Name"))
    gen_value_type = models.CharField(max_length=1,choices=Genearl_Type_CHOICES, verbose_name=_("General Value Type"))
    status =  models.ForeignKey(Status,  on_delete=models.CASCADE, verbose_name=_("Status"))
    created_by = CreatingUserField(related_name = "PhysicalGeneralMasterCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "PhysicalGeneralMasterUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.gen_name
    
    class Meta:
        verbose_name = "Physical General Master"
        verbose_name_plural = "Physical General Master"
        db_table = 'ccrh_phy_general_master'
        
#Past History Creating table starts here    
class PastHistoryType(models.Model):
    his_type_name = models.CharField(max_length=100, verbose_name=_("History Type Name"))
    status =  models.ForeignKey(Status,  on_delete=models.CASCADE, verbose_name=_("Status"))
    created_by = CreatingUserField(related_name = "PastHistoryTypeCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "PastHistoryTypeUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.his_type_name
    
    class Meta:
        verbose_name = "Past History Type "
        verbose_name_plural = "Past History Type"
        db_table = 'ccrh_past_history_type'
        
#Past History Master Creating table starts here    
class PastHistoryMaster(models.Model):
    his_type = models.ForeignKey(PastHistoryType,  on_delete=models.CASCADE, verbose_name=_("History Type"))
    his_name = models.CharField(max_length=100, verbose_name=_("History Name"))
    status =  models.ForeignKey(Status,  on_delete=models.CASCADE, verbose_name=_("Status"))
    created_by = CreatingUserField(related_name = "PastHistoryMasterCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "PastHistoryMasterUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.his_name
    
    class Meta:
        verbose_name = "Past History Master"
        verbose_name_plural = "Past History Master"
        db_table = 'ccrh_past_hisory_master'

#Physical Finding Type Creating table starts here    
class PhysicalFindingType(models.Model):
    find_type = models.CharField(max_length=100, verbose_name=_("Physical Find Type"), unique=True)
    status =  models.ForeignKey(Status,  on_delete=models.CASCADE, verbose_name=_("Status"))
    created_by = CreatingUserField(related_name = "PhysicalFindingTypeCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "PhysicalFindingTypeUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.find_type
    
    class Meta:
        verbose_name = "Physical Finding Type"
        verbose_name_plural = "Physical Finding Type"
        db_table = 'ccrh_phy_finding_type'

 #Physical Finding Measurement Creating table starts here    
class PhysicalFindingMeasurementMaster(models.Model):
    measurement = models.CharField(max_length=100, verbose_name=_("Measurement"), unique=True)
    status =  models.ForeignKey(Status,  on_delete=models.CASCADE, verbose_name=_("Status"))
    created_by = CreatingUserField(related_name = "PhysicalFindingMeasurementMasterCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "PhysicalFindingMeasurementMasterUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.measurement

    class Meta:
        verbose_name = "Physical Finding Measurement Master"
        verbose_name_plural = "Physical Finding Measurement Master"
        db_table = 'ccrh_phy_finding_measurement_master'      

#Physical Finding Master Creating table starts here    
class PhysicalFindingMaster(models.Model):
    fin_type = models.ForeignKey(PhysicalFindingType,  on_delete=models.CASCADE, verbose_name=_("Physical Find Type"))
    find_name = models.CharField(max_length=100, verbose_name=_("Physical Find Name"))
    measure = models.ForeignKey(PhysicalFindingMeasurementMaster,  on_delete=models.CASCADE, verbose_name=_("Physical Find Measurement"))
    status =  models.ForeignKey(Status,  on_delete=models.CASCADE, verbose_name=_("Status"))
    created_by = CreatingUserField(related_name = "PhysicalFindingMasterCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "PhysicalFindingMasterUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.find_name
    
    class Meta:
        verbose_name = "Physical Finding Master"
        verbose_name_plural = "Physical Finding Master"
        db_table = 'ccrh_phy_finding_master'
        
# Miasamatic Analysis Master Creating table starts here    
class MiasamaticAnalysisMaster(models.Model):
    mia_analys_name = models.CharField(max_length=100, verbose_name=_("Miasamatic Analysis Name"))
    status =  models.ForeignKey(Status,  on_delete=models.CASCADE, verbose_name=_("Status"))
    created_by = CreatingUserField(related_name = "MiasamaticAnalysisMasterCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "MiasamaticAnalysisMasterUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.mia_analys_name
    
    class Meta:
        verbose_name = "Miasamatic Analysis Master"
        verbose_name_plural = "Miasamatic Analysis Master"
        db_table = 'ccrh_miasamatic_analysis_master'
        
# Addon Therapy Master Creating table starts here    
class AddonTherapyMaster(models.Model):
    thrpy_name = models.CharField(max_length=100, verbose_name=_("Therapy Name"))
    status =  models.ForeignKey(Status,  on_delete=models.CASCADE, verbose_name=_("Status"))
    created_by = CreatingUserField(related_name = "AddonTherapyMasterCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "AddonTherapyMasterUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.thrpy_name
    
    class Meta:
        verbose_name = "Addon Therapy Master"
        verbose_name_plural = "Addon Therapy Master"
        db_table = 'ccrh_addon_therapy_master'
        