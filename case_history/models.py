from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User, Group
from audit_log.models.fields import CreatingUserField, LastUserField
from django.db.models.deletion import CASCADE
from random import choices
from master.models import (State,City,Status,ClinicalSetting,DiseaseMaster,
                           SymptomsMaster,PastHistoryMaster,PhysicalFindingMaster,
                           MedicineMaster,SymptomsMaster,PhysicalGeneralMaster,
                          MiasamaticAnalysisMaster, HabitMaster,AddonTherapyMaster,
                          InvestigationsMaster)
from user_profile.models import (PractDetails)

# Create your models here.

class CaseCategory(models.Model):
    category_name = models.CharField(max_length=50, verbose_name=_("Category Name"))
    created_by = CreatingUserField(related_name = "CaseCategoryCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "CaseCategoryUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.category_name
    
    class Meta:
        verbose_name = "Case Category"
        verbose_name_plural = "Case Category"
        db_table = 'case_category'
        
class CaseStatus(models.Model):
    cstatus_name = models.CharField(max_length=50, verbose_name=_("Case Status Name"))
    created_by = CreatingUserField(related_name = "CaseStatusCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "CaseStatusUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.cstatus_name
    
    class Meta:
        verbose_name = "Case Status"
        verbose_name_plural = "Case Status"
        db_table = 'case_status'

class CaseReviewStatus(models.Model):
    review_status_name = models.CharField(max_length=50, verbose_name=_("Case Review Status Name"))
    created_by = CreatingUserField(related_name = "CaseReviewStatusCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "CaseReviewStatusUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.review_status_name
    
    class Meta:
        verbose_name = "Case Review Status"
        verbose_name_plural = "Case Review Status"
        db_table = 'case_review_status'

class CaseListingStatus(models.Model):
    listing_status_name = models.CharField(max_length=50, verbose_name=_("Case Listing Status Name"))
    created_by = CreatingUserField(related_name = "CaseListingStatusCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "CaseListingStatusUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.listing_status_name
    
    class Meta:
        verbose_name = "Case Listing Status"
        verbose_name_plural = "Case Listing Status"
        db_table = 'case_listing_status'
        
        
class CaseCheckListMaster(models.Model):
    checklist_name = models.CharField(max_length=50, verbose_name=_("CheckList Name"))
    created_by = CreatingUserField(related_name = "CaseCheckListMasterCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "CaseCheckListMasterUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.checklist_name
    
    class Meta:
        verbose_name = "Case CheckList Master"
        verbose_name_plural = "Case CheckList Master"
        db_table = 'case_checklist_master'
        

class CaseHistory(models.Model):
    Religion_CHOICES = (
        (u'1', u'Hindu'),
        (u'2', u'Muslim'),
        (u'3', u'Christian'),
        (u'4', u'Sikhs'),
        (u'5', u'Jain'),
        (u'6', u'Buddhists'),
        (u'8', u'Others'),
    )
    Economy_CHOICES = (
        (u'1', u'Lower'),
        (u'2', u'Middle'),
        (u'3', u'Higher'),
    )
    Gender_CHOICES = (
            (u'1', u'Male'),
            (u'2', u'Female'),
            (u'3', u'Others'),
        )
    case_title = models.CharField(max_length=150, verbose_name=_("Case Title"))
    case_keywords =  models.TextField( blank=True, null=True, verbose_name=_("Case Keywords"))
    case_summary = models.CharField(max_length=250, verbose_name=_("Case Summary"))
    case_pract = models.ForeignKey(PractDetails,  on_delete=models.CASCADE, verbose_name=_("Case Pract"))
    case_patient_name =  models.CharField(max_length=100, verbose_name=_("Case Patient Name"))
    case_patient_mobile  = models.BigIntegerField(blank=True, null=True, verbose_name=_("Patient Mobile Number ")) 
    case_patient_email = models.CharField(blank=True, null=True, max_length=100, verbose_name=_("Patient Email"))
    case_patient_age =  models.IntegerField(verbose_name=_("Patient Age"))
    case_patient_sex = models.CharField(max_length=1,choices=Gender_CHOICES, verbose_name=_("Patient Sex"))
    case_patient_address = models.TextField(  verbose_name=_("Patient Address"))
    case_patient_city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name=_("City Name"))
    case_patient_state = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name=_("State Name"))
    case_patient_occupation = models.CharField(max_length=100, verbose_name=_("Patient Occupation"))
    case_patient_religion =  models.CharField(max_length=1,choices=Religion_CHOICES, verbose_name=_("Patient Religion"))
    case_patient_economy_status = models.CharField(max_length=1,choices=Economy_CHOICES, verbose_name=_("Patient Economy Status"))
    category = models.ForeignKey(CaseCategory, on_delete=models.CASCADE, verbose_name=_("Case Category"))
    case_status = models.ForeignKey(CaseStatus, on_delete=models.CASCADE, verbose_name=_("Case Status"))
    case_reviewer = models.ForeignKey(User, blank=True,null=True, on_delete=models.CASCADE, verbose_name=_("Case Reviewer"))
    case_listing_status =  models.ForeignKey(CaseListingStatus,  on_delete=models.CASCADE, verbose_name=_("Case Listing Status"))
    case_review_status = models.ForeignKey(CaseReviewStatus, on_delete=models.CASCADE, verbose_name=_("Case Review Status"))
    created_by = CreatingUserField(related_name = "CaseHistoryCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "CaseHistoryUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.case_title
    
    class Meta:
        verbose_name = "Case History "
        verbose_name_plural = "Case History"
        db_table = 'ccrh_case_history'

class CaseDiagnosis(models.Model):
    PRIMARY_CHOICES = (
            (u'1', u'Yes'),
            (u'0', u'No'),
        )
    case =  models.ForeignKey(CaseHistory,  on_delete=models.CASCADE, verbose_name=_("Case History"))
    dis =  models.ForeignKey(DiseaseMaster,  on_delete=models.CASCADE, verbose_name=_("Case Disease"))
    is_primary = models.CharField(max_length=1, choices=PRIMARY_CHOICES, verbose_name=_("Is Primary"), default=0)
    created_by = CreatingUserField(related_name = "CaseDiagnosisCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "CaseDiagnosisUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.case.case_title
    
    class Meta:
        verbose_name = "Case Diagnosis"
        verbose_name_plural = "Case Diagnosis"
        db_table = 'ccrh_case_diagnosis'
        

class CaseComplaints(models.Model):
    Duration_CHOICES = (
        (u'1', u'days'),
        (u'2', u'month'),
        (u'3', u'year'),
    )
    case =  models.ForeignKey(CaseHistory,  on_delete=models.CASCADE, verbose_name=_("Case History"))
    comp_symptoms =  models.ForeignKey(SymptomsMaster,  on_delete=models.CASCADE, verbose_name=_("Case Symptoms"))
    comp_duration = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Complaint Duration"))
    comp_duration_type = models.CharField(max_length=1,choices=Duration_CHOICES, verbose_name=_("Complaints Duration Type"))
    comp_side = models.TextField(blank=True,null=True,  verbose_name=_("Complaints Side"))
    comp_time = models.TextField(blank=True,null=True,  verbose_name=_("Complaints Time"))
    comp_modality =  models.TextField(blank=True,null=True,  verbose_name=_("Complaints Modality"))
    comp_extension = models.TextField(blank=True,null=True,  verbose_name=_("Complaints Extension"))
    created_by = CreatingUserField(related_name = "CaseComplaintsCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "CaseComplaintsUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.comp_side
    
    class Meta:
        verbose_name = "Case Complaints"
        verbose_name_plural = "Case Complaints"
        db_table = 'ccrh_case_complaints'
        
class CasePersonalHistory(models.Model):
    Hab_Value_CHOICES = (
        (u'1', u'Yes'),
        (u'2', u'No'),
    )
    Phis_Duration_CHOICES= (
        (u'1', u'days'),
        (u'2', u'month'),
        (u'3', u'year'),
    )
    case =  models.ForeignKey(CaseHistory,  on_delete=models.CASCADE, verbose_name=_("Case History"))
    hab =  models.ForeignKey(HabitMaster,  on_delete=models.CASCADE, verbose_name=_("Habit"))
    phis_duration = models.DecimalField(blank=True,null=True, max_digits=10, decimal_places=2, verbose_name=_("Physical Duration"))
    phis_hab_value = models.CharField(max_length=1,choices=Hab_Value_CHOICES, verbose_name=_("Physical Habit Value"))
    phis_duration_type = models.CharField(max_length=1,blank=True,null=True,choices=Phis_Duration_CHOICES, verbose_name=_("Physical Duration Type"))
    phis_consumption_pattern =  models.CharField(max_length=100,blank=True,null=True, verbose_name=_("Consumption Pattern"))
    created_by = CreatingUserField(related_name = "CasePersonalHistoryCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "CasePersonalHistoryUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.case.case_title
    
    class Meta:
        verbose_name = "Case Personal History"
        verbose_name_plural = "Case Personal History"
        db_table = 'ccrh_case_personal_history'
        
                        
class CasePhysicalGeneral(models.Model):
    case =  models.ForeignKey(CaseHistory,  on_delete=models.CASCADE, verbose_name=_("Case History "))
    hab =  models.ForeignKey(PhysicalGeneralMaster,  on_delete=models.CASCADE, verbose_name=_("Habbit "))
    phygen_value =  models.CharField(max_length=100, verbose_name=_("Physical General Value"))
    created_by = CreatingUserField(related_name = "CasePhysicalGeneralCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "CasePhysicalGeneralUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.case.case_title
    
    class Meta:
        verbose_name = "Case Physical General"
        verbose_name_plural = "Case Physical General"
        db_table = 'ccrh_case_physical_general'


class CaseMentalGeneral(models.Model):
    case =  models.ForeignKey(CaseHistory,  on_delete=models.CASCADE, verbose_name=_("Case History "))
    ment_gen_value =  models.TextField( verbose_name=_("Mental General Value"))
    created_by = CreatingUserField(related_name = "CaseMentalGeneralCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "CaseMentalGeneralUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.ment_gen_value
    
    class Meta:
        verbose_name = "Case Mental General"
        verbose_name_plural = "Case Mental General"
        db_table = 'ccrh_case_mental_general'
        
class CasePastHistoryDisease(models.Model):
    case =  models.ForeignKey(CaseHistory, on_delete=models.CASCADE, verbose_name=_("Case History "))
    dis =  models.ForeignKey(DiseaseMaster, on_delete=models.CASCADE, verbose_name=_("Disease Name "))
    his_dis_yronset = models.TextField( verbose_name=_("Disease Yronset"))
    his_dis_ageonset = models.TextField( verbose_name=_("Disease Ageonset"))
    his_dis_trthistory = models.TextField(verbose_name=_("Disease Trthistory"), blank=True, null=True)
    his_dis_outcome =  models.TextField(verbose_name=_("Disease Outcome"), blank=True, null=True)
    created_by = CreatingUserField(related_name = "CasePastHistoryDiseaseCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "CasePastHistoryDiseaseUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.case.case_title
    
    class Meta:
        verbose_name = "Case Past History Disease"
        verbose_name_plural = "Case Past History Disease"
        db_table = 'ccrh_case_past_history_disease'
        
        
class CasePastHistory(models.Model):
    case =  models.ForeignKey(CaseHistory,  on_delete=models.CASCADE, verbose_name=_("Case History "))
    his_mas =  models.ForeignKey(PastHistoryMaster,  on_delete=models.CASCADE, verbose_name=_("Past History"))
    phist_value =  models.TextField(verbose_name=_("Physical Value"))
    created_by = CreatingUserField(related_name = "CasePaseHistoryCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "CasePastHistoryUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.case.case_title
    
    class Meta:
        verbose_name = "Case Past History "
        verbose_name_plural = "Case Past History"
        db_table = 'ccrh_case_past_history'
        
        
        
class CaseFamilyHistory(models.Model):
    Alive_Dead_CHOICES= (
        (u'1', u'Alive'),
        (u'2', u'Dead'),
    )
    case =  models.ForeignKey(CaseHistory,  on_delete=models.CASCADE, verbose_name=_("Case History "))
    famil_his_alive_dead = models.CharField(max_length=1,choices=Alive_Dead_CHOICES, verbose_name=_("Alive Or Dead"))
    famil_his_relation =  models.CharField(max_length=100, verbose_name=_("Family Relation"))
    dis =  models.ForeignKey(DiseaseMaster, blank=True,null=True, on_delete=models.CASCADE, verbose_name=_("Case Disease"))
    created_by = CreatingUserField(related_name = "CaseFamilyHistoryCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "CaseFamilyHistoryUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.famil_his_relation
    
    class Meta:
        verbose_name = "Case Family History"
        verbose_name_plural = "Case Family History"
        db_table = 'ccrh_case_family_history'
        
class GynaecologicalHistory(models.Model):
    Leucorrhea_CHOICES = (
        (u'1', u'quantity'),
        (u'2', u'color'),
        (u'3', u'consistency'),
        (u'4', u'others'),
    )
    Character_CHOICES = (
        (u'1', u'acrid'),
        (u'2', u'bland'),
    )
    Odur_CHOICES = (
        (u'1', u'odourless'),
        (u'2', u'offensive'),
    )
    Color_CHOICES = (
        (u'1', u'brightred'),
        (u'2', u'darkred'),
        (u'3', u'black'),
    )
    Quantity_CHOICES = (
        (u'1', u'profuse'),
        (u'2', u'scanty'),
        (u'3', u'normal'),
    )
    case = models.ForeignKey(CaseHistory,  on_delete=models.CASCADE, verbose_name=_("Case History "))
    menarche_date_age = models.CharField(max_length=15,blank=True,null=True, verbose_name=_("Menarche Date Age"))
    menst_lmp =  models.CharField(max_length=10, verbose_name=_("Menst Imp"))
    menst_cycle =  models.CharField(max_length=10, verbose_name=_("Menst Cycle"))
    menst_duration =  models.CharField(max_length=10, verbose_name=_("Menst Duration"))
    menst_quantity =  models.CharField(max_length=1,choices=Quantity_CHOICES, verbose_name=_("Menst Quantity"))
    menst_colour = models.CharField(max_length=1, choices=Color_CHOICES, verbose_name=_("Menst Color"))
    menst_odur = models.CharField(max_length=1, choices=Odur_CHOICES, verbose_name=_("Menst Odur"))
    menst_character = models.CharField(max_length=1, choices=Character_CHOICES, verbose_name=_("Menst Character"))
    menst_complaints_b_d_a_menses = models.TextField(verbose_name=_("Ments Complaints B D A Menses"))
    menst_leucorrhea = models.CharField(max_length=1, choices=Leucorrhea_CHOICES, verbose_name=_("Menst Leucorrhea"))
    menst_surgery = models.TextField(verbose_name=_("Ments Surgery"))
    created_by = CreatingUserField(related_name = "GynaecologicalHistoryCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "GynaecologicalHistoryUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.menst_lmp
    
    class Meta:
        verbose_name = "Gynaecological History "
        verbose_name_plural = "Gynaecological History"
        db_table = 'ccrh_case_gynaecological_history'
        
class CaseObstrericHistory(models.Model):
    case =  models.ForeignKey(CaseHistory, on_delete=models.CASCADE, verbose_name=_("Case History "))
    pbh_his_gravida = models.TextField(blank=True,null=True,verbose_name=_("Pbh Histroy Gravida"))
    pbh_his_para = models.TextField(blank=True,null=True,verbose_name=_("Pbh Histroy Para"))
    pbh_his_abortion = models.TextField(blank=True,null=True,verbose_name=_("Pbh Histroy Abortion"))
    pbh_his_stillbirth = models.TextField(blank=True,null=True,verbose_name=_("Pbh Histroy Stillbirth"))
    pbh_his_living = models.TextField(blank=True,null=True,verbose_name=_("Pbh Histroy living"))
    pbh_his_period_of_pregnancy = models.TextField(blank=True,null=True,verbose_name=_("Pbh Histroy Pregnancy"))
    pbh_his_lactation_history = models.TextField(blank=True,null=True,verbose_name=_("Pbh Histroy Lactation History"))
    pbh_his_comp_dur_pregnancy = models.TextField(blank=True,null=True,verbose_name=_("Pbh Histroy Comp Dur Pregnancy"))
    pbh_his_nature_of_labor = models.TextField(blank=True,null=True,verbose_name=_("Pbh Histroy Nature of Labour"))
    pbh_his_nature_of_delivery = models.TextField(blank=True,null=True,verbose_name=_("Pbh Histroy Nature of Delivery"))
    pbh_his_nature_of_puerperium = models.TextField(blank=True,null=True,verbose_name=_("Pbh Histroy Nature of Puerperium"))
    created_by = CreatingUserField(related_name = "CaseObstrericHistoryCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "CaseObstrericHistoryUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.case.case_title
    
    class Meta:
        verbose_name = "Case Obstreric History"
        verbose_name_plural = "Case Obstreric History"
        db_table = 'ccrh_case_obstreric_history'
        
class CaseObstrericChildHistory(models.Model):
    Child_Alive_CHOICES = (
        (u'1', u'Yes'),
        (u'2', u'No'),
    )
    case =  models.ForeignKey(CaseHistory,  on_delete=models.CASCADE, verbose_name=_("Case History "))
    chd_his_child = models.TextField(verbose_name=_("Child history"))
    chd_his_alive = models.CharField(max_length=1, default=1, choices=Child_Alive_CHOICES, verbose_name=_("Is Alive"))
    chd_his_causeofdeath =  models.TextField(blank=True,null=True, verbose_name=_("Cause of Death"))
    chd_his_birthweight =  models.TextField(blank=True,null=True, verbose_name=_("Bright Weight"))
    created_by = CreatingUserField(related_name = "CaseObstrericChildHistoryCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "CaseObstrericChildHistoryUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.chd_his_child
    
    class Meta:
        verbose_name = "Obstreric Child History  "
        verbose_name_plural = "Obstreric Child History  "
        db_table = 'ccrh_case_obstreric_child_history'
        
class CasePhysicalFindings(models.Model):
    case =  models.ForeignKey(CaseHistory, on_delete=models.CASCADE, verbose_name=_("Case History "))
    fin_mas =  models.ForeignKey(PhysicalFindingMaster,  on_delete=models.CASCADE, verbose_name=_("Physical Finding"))
    phyfind_value = models.TextField(verbose_name=_("Physical Find Value"))
    created_by = CreatingUserField(related_name = "CasePhysicalFindingsCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "CasePhysicalFindingsUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.phyfind_value
    
    class Meta:
        verbose_name = "Physical Findings"
        verbose_name_plural = "Physical Findings"
        db_table = 'ccrh_case_phyc_findings'
        
class CaseRepertorisation(models.Model):
    Rep_Analysis_CHOICES = (
        (u'1', u'Yes'),
        (u'2', u'No'),
    )
    case =  models.ForeignKey(CaseHistory, on_delete=models.CASCADE, verbose_name=_("Case History"))
    rep_document = models.FileField(verbose_name=_("Repertorisation  Document"))
    rep_analysis = models.CharField(max_length=1,default=1, choices=Rep_Analysis_CHOICES, verbose_name=_("Repesntation Analysis"))
    created_by = CreatingUserField(related_name = "CaseRepertorisationCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "CaseRepertorisationUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.rep_analysis
    
    class Meta:
        verbose_name = "Case Repertorisation "
        verbose_name_plural = "Case repertorisation "
        db_table = 'ccrh_case_repertorisation'
        
class CaseMiasamaticAnalysis(models.Model):
    Mia_Analysis_CHOICES = (
        (u'1', u'Yes'),
        (u'2', u'No'),
    )
    case =  models.ForeignKey(CaseHistory,  on_delete=models.CASCADE, verbose_name=_("Case History"))
    mia_analys_mas = models.ForeignKey(MiasamaticAnalysisMaster,  on_delete=models.CASCADE, verbose_name=_("Miasamatic Analysis"))
    mia_analys_value = models.CharField(max_length=1, choices=Mia_Analysis_CHOICES, verbose_name=_(" Miasamatic Analysis Value"))
    created_by = CreatingUserField(related_name = "CaseMiasamaticAnalysisCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "CaseMiasamaticAnalysisUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.mia_analys_mas.mia_analys_name
    
    class Meta:
        verbose_name = "Case Miasamatic Analysis  "
        verbose_name_plural = "Case Miasamatic Analysis "
        db_table = 'ccrh_case_miasamatic_analysis'
        

class CaseMedicineManagement(models.Model):
    Presc_Order_CHOICES = (
        (u'1', u'1'),
        (u'2', u'2'),
        (u'3', u'3'),
        (u'4', u'4'),
        (u'5', u'5'),
        (u'6', u'6'),
        (u'7', u'7'),
    )
    case =  models.ForeignKey(CaseHistory,  on_delete=models.CASCADE, verbose_name=_("Case History "))
    prescription_date = models.DateField(verbose_name=_("Prescription Date"))
    prescription_order = models.CharField(max_length=1,default=1, choices=Presc_Order_CHOICES, verbose_name=_(" Prescription Order"))
    prescription_oridl_scale = models.TextField(blank=True,null=True,verbose_name=_(" Prescription oridl Scale"))
    outcome_of_prev_presc = models.TextField(blank=True,null=True,verbose_name=_("Outcome of Previous Prescription "))
    marks_for_improvement = models.TextField(blank=True,null=True,verbose_name=_("Marks for Improvement "))
    created_by = CreatingUserField(related_name = "CaseMedicineManagementCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "CaseMedicineManagementUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.case.case_title
    
    class Meta:
        verbose_name = "Case Medicine Management"
        verbose_name_plural = "Case Medicine Management "
        db_table = 'ccrh_case_medicine_management'
        
class MedicinePrescriptionMapping(models.Model):
    medi_mgnt =  models.ForeignKey(CaseMedicineManagement,  on_delete=models.CASCADE, verbose_name=_("Medical Management"))
    prescription =  models.ForeignKey(MedicineMaster,  on_delete=models.CASCADE, verbose_name=_("Prescription"))
    potency = models.CharField(max_length=50, verbose_name=_("Potency"))
    dosage = models.CharField(max_length=50, verbose_name=_("Dosage"))
    created_by = CreatingUserField(related_name = "MedicinePrescriptionMappingCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "MedicinePrescriptionMappingUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.prescription.med_name
    
    class Meta:
        verbose_name = "Medicine Prescription Mapping"
        verbose_name_plural = "Medicine Prescription Mapping"
        db_table = 'ccrh_medicine_prescription_mapping'
        
class PrescriptionSymptomMapping(models.Model):
    medi_pres_map =  models.ForeignKey(MedicinePrescriptionMapping,  on_delete=models.CASCADE, verbose_name=_("Medical Prescription "))
    symptom =  models.ForeignKey(SymptomsMaster,  on_delete=models.CASCADE, verbose_name=_("Symptoms"))
    created_by = CreatingUserField(related_name = "PrescriptionSymptomMappingCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "PrescriptionSymptomMappingUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.symptom.sym_name
    
    class Meta:
        verbose_name = "Prescription Symptom Mapping"
        verbose_name_plural = "Prescription Symptom Mapping"
        db_table = 'ccrh_prescription_symptom_mapping'

class CaseAddonTherapy(models.Model):
    Duration_Temper_CHOICES = (
        (u'1', u'Yes'),
        (u'2', u'No'),
    )
    case =  models.ForeignKey(CaseHistory,  on_delete=models.CASCADE, verbose_name=_("Case History "))
    addon_thrpy_mas = models.ForeignKey(AddonTherapyMaster,  on_delete=models.CASCADE, verbose_name=_("Addon Thearpy "))
    duration_tamper_homeo = models.CharField(max_length=1,default=1, choices=Duration_Temper_CHOICES, verbose_name=_(" Duration Temper Homeo"))
    medicine_name = models.CharField(max_length=100,blank=True,null=True,verbose_name=_(" Medicine Name"))
    medicine_dosage = models.CharField(max_length=100,blank=True,null=True,verbose_name=_("Medicine Dosage "))
    created_by = CreatingUserField(related_name = "CaseAddonTherapyCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "CaseAddonTherapyUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.addon_thrpy_mas.thrpy_name
    
    class Meta:
        verbose_name = "Case Addon Therapy"
        verbose_name_plural = "Case Addon Therapy "
        db_table = 'ccrh_case_addon_therapy '

class CaseInvestigation(models.Model):
    case =  models.ForeignKey(CaseHistory,  on_delete=models.CASCADE, verbose_name=_("Case History "))
    investg_mas =  models.ForeignKey(InvestigationsMaster,  on_delete=models.CASCADE, verbose_name=_("Investigation"))
    investg_value =  models.TextField( blank=True, null=True, verbose_name=_("Investigation Value"))
    investg_file = models.FileField( blank=True, null=True, verbose_name=_("Investigation File"))
    created_by = CreatingUserField(related_name = "CaseInvestigationCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "CaseInvestigationUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.investg_mas.investg_name
    
    class Meta:
        verbose_name = "Case Investigation"
        verbose_name_plural = "Case Investigation"
        db_table = 'ccrh_case_investigation'

class CaseStatusHistory(models.Model):
    case =  models.ForeignKey(CaseHistory,  on_delete=models.CASCADE, verbose_name=_("Case History "))
    case_status  =  models.ForeignKey(CaseStatus,  on_delete=models.CASCADE, verbose_name=_("Case Status"))
    case_remarks =  models.TextField( verbose_name=_("Case Remarks"))
    created_by = CreatingUserField(related_name = "CaseStatusHistoryCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "CaseStatusHistoryUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.case_status.cstatus_name
    
    class Meta:
        verbose_name = "Case Status History"
        verbose_name_plural = "Case Status History"
        db_table = 'ccrh_case_status_history'
        
class CaseReviewStatusHistory(models.Model):
    case =  models.ForeignKey(CaseHistory,  on_delete=models.CASCADE, verbose_name=_("Case History "))
    case_review_status  =  models.ForeignKey(CaseReviewStatus,  on_delete=models.CASCADE, verbose_name=_("Case Review Status"))
    case_review_remarks =  models.TextField( verbose_name=_("Case Review Remarks"))
    created_by = CreatingUserField(related_name = "CaseReviewStatusHistoryCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "CaseReviewStatusHistoryUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.case_review_status.review_status_name
    
    class Meta:
        verbose_name = "Case Review Status History"
        verbose_name_plural = "Case Review Status History"
        db_table = 'ccrh_case_review_status_history'
        
        
class CaseChecklistMapping(models.Model):
    Checklist_CHOICES =  (
        (u'1', u'Yes'),
        (u'0', u'No'),
    )
    case =  models.ForeignKey(CaseHistory,  on_delete=models.CASCADE, verbose_name=_("Case History "))
    checklist  =  models.ForeignKey(CaseCheckListMaster,  on_delete=models.CASCADE, verbose_name=_("Case CheckList"))
    checklist_value =  models.CharField(max_length=1, choices=Checklist_CHOICES, verbose_name=_("Checklist Value"))
    created_by = CreatingUserField(related_name = "CaseChecklistMappingCreatedBy")
    created_date = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_by = LastUserField(related_name = "CaseChecklistMappingUpdatedBy")
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.checklist.checklist_name
    
    class Meta:
        verbose_name = "Case Checklist Mapping"
        verbose_name_plural = "Case Checklist Mapping"
        db_table = 'ccrh_case_checklist_mapping'