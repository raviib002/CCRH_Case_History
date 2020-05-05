from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget, DateTimeWidget, IntegerWidget
from import_export.admin import ImportMixin, ExportMixin, ImportExportMixin
from import_export.formats import base_formats
from django.forms import forms, ModelForm, Select
from import_export import resources, fields
from master.models import (State,City,Status,ClinicalSetting,DiseaseMaster,
                           SymptomsMaster,PastHistoryMaster,PhysicalFindingMaster,
                           MiasamaticAnalysisMaster,MedicineMaster,SymptomsMaster,PhysicalGeneralMaster,
                            HabitMaster,AddonTherapyMaster,
                           InvestigationsMaster)
from user_profile.models import PractDetails
from case_history.models import (CaseCategory,
                                 CaseStatus,
                                 CaseReviewStatus,
                                 CaseListingStatus,
                                 CaseCheckListMaster,
                                 CaseHistory,
                                 CaseDiagnosis,
                                 CaseComplaints,
                                 CasePersonalHistory,
                                 CasePhysicalGeneral,
                                 CaseMentalGeneral,
                                 CasePastHistoryDisease,
                                 CasePastHistory,
                                 CaseFamilyHistory,
                                 GynaecologicalHistory,
                                 CaseObstrericHistory,
                                 CaseObstrericChildHistory,
                                 CasePhysicalFindings,
                                 CaseRepertorisation,
                                 CaseMiasamaticAnalysis,
                                 CaseMedicineManagement,
                                 MedicinePrescriptionMapping,
                                 PrescriptionSymptomMapping,
                                 CaseAddonTherapy,
                                 CaseInvestigation,
                                 CaseStatusHistory,
                                 CaseReviewStatusHistory,
                                 CaseChecklistMapping,
                                )

#CaseCategory admin starts here
class CaseCategoryResource(resources.ModelResource):
    category_name = fields.Field(column_name=_('Category Name'), attribute='category_name')
     
    class Meta:
        model = CaseCategory
        fields = ('category_name',)
        import_id_fields = fields
        export_order = fields
     
     
class CaseCategoryAdmin(ImportExportModelAdmin):
    resource_class = CaseCategoryResource
    list_display = ('category_name',)
    search_fields = ('category_name',)
    list_filter = ('category_name',)
#CaseCategory admin ends here

#CaseStatus admin starts here
class CaseStatusResource(resources.ModelResource):
    cstatus_name = fields.Field(column_name=_('Case Status Name'), attribute='cstatus_name')
     
    class Meta:
        model = CaseStatus
        fields = ('cstatus_name',)
        import_id_fields = fields
        export_order = fields
     
     
class CaseStatusAdmin(ImportExportModelAdmin):
    resource_class = CaseStatusResource
    list_display = ('cstatus_name',)
    search_fields = ('cstatus_name',)
    list_filter = ('cstatus_name',)
#CaseStatus admin ends here

#CaseReviewStatus admin starts here
class CaseReviewStatusResource(resources.ModelResource):
    review_status_name = fields.Field(column_name=_('Case Review Status Name'), attribute='review_status_name')
     
    class Meta:
        model = CaseReviewStatus
        fields = ('review_status_name',)
        import_id_fields = fields
        export_order = fields
     
     
class CaseReviewStatusAdmin(ImportExportModelAdmin):
    resource_class = CaseReviewStatusResource
    list_display = ('review_status_name',)
    search_fields = ('review_status_name',)
    list_filter = ('review_status_name',)
#CaseReviewStatus admin ends here

#CaseListingStatus admin starts here
class CaseListingStatusResource(resources.ModelResource):
    listing_status_name = fields.Field(column_name=_('Case Listing Status Name'), attribute='listing_status_name')
     
    class Meta:
        model = CaseListingStatus
        fields = ('listing_status_name',)
        import_id_fields = fields
        export_order = fields
     
     
class CaseListingStatusAdmin(ImportExportModelAdmin):
    resource_class = CaseListingStatusResource
    list_display = ('listing_status_name',)
    search_fields = ('listing_status_name',)
    list_filter = ('listing_status_name',)
#CaseListingStatus admin ends here

#CaseCheckListMaster admin starts here
class CaseCheckListMasterResource(resources.ModelResource):
    checklist_name = fields.Field(column_name=_('CheckList Name'), attribute='checklist_name')
     
    class Meta:
        model = CaseCheckListMaster
        fields = ('checklist_name',)
        import_id_fields = fields
        export_order = fields
     
     
class CaseCheckListMasterAdmin(ImportExportModelAdmin):
    resource_class = CaseCheckListMasterResource
    list_display = ('checklist_name',)
    search_fields = ('checklist_name',)
    list_filter = ('checklist_name',)
#CaseCheckListMaster admin ends here

#CaseHistory admin starts here
class CaseHistoryResource(resources.ModelResource):
    case_title = fields.Field(column_name=_('Case Title'), attribute='case_title')
    case_keywords = fields.Field(column_name=_('Case Keywords'), attribute='case_keywords')
    case_summary = fields.Field(column_name=_('Case Summary'), attribute='case_summary')
    case_pract = fields.Field(column_name=_('Case Pract'), attribute='case_pract',)
    case_patient_name = fields.Field(column_name=_('Case Patient Name'), attribute='case_patient_name')
    case_patient_mobile = fields.Field(column_name=_('Patient Mobile Number'), attribute='case_patient_mobile')
    case_patient_email = fields.Field(column_name=_('Patient Email'), attribute='case_patient_email')
    case_patient_age = fields.Field(column_name=_('Patient Age'), attribute='case_patient_age')
    case_patient_sex = fields.Field(column_name=_('Patient Sex'), attribute='case_patient_sex')
    case_patient_address = fields.Field(column_name=_('Patient Address'), attribute='case_patient_address')
    case_patient_city = fields.Field(column_name=_('City Name'), attribute='case_patient_city')
    case_patient_state = fields.Field(column_name=_('State Name'), attribute='case_patient_state')
    case_patient_occupation = fields.Field(column_name=_('Patient Occupation'), attribute='case_patient_occupation')
    case_patient_religion = fields.Field(column_name=_('Patient Religion'), attribute='case_patient_religion')
    case_patient_economy_status = fields.Field(column_name=_('Patient Economy Status'), attribute='case_patient_economy_status')
    category = fields.Field(column_name=_('Case Category'), attribute='category')
    case_status = fields.Field(column_name=_('Case Status'), attribute='case_status')
    case_reviewer = fields.Field(column_name=_('Case Reviewer'), attribute='case_reviewer')
    case_listing_status = fields.Field(column_name=_('Case Listing Status'), attribute='case_listing_status')
    case_review_status = fields.Field(column_name=_('Case Review Status'), attribute='case_review_status')
     
    class Meta:
        model = CaseHistory
        fields = ('case_title','case_keywords','case_summary','case_pract','case_patient_name','case_patient_mobile','case_patient_email','case_patient_age',
                  'case_patient_sex','case_patient_address','case_patient_city','case_patient_state','case_patient_occupation','case_patient_religion','case_patient_economy_status',
                  'category','case_status','case_reviewer','case_listing_status','case_review_status',)
        import_id_fields = fields
        export_order = fields
     
     
class CaseHistoryAdmin(ImportExportModelAdmin):
    resource_class = CaseHistoryResource
    list_display = ('case_title','case_keywords','case_summary','case_pract','case_patient_name','case_patient_mobile','case_patient_email','case_patient_age',
                  'case_patient_sex','case_patient_address','case_patient_city','case_patient_state','case_patient_occupation','case_patient_religion','case_patient_economy_status',
                  'category','case_status','case_reviewer','case_listing_status','case_review_status',)
    search_fields = ('case_title','case_keywords','case_summary','case_pract_id','case_patient_name','case_patient_mobile','case_patient_email','case_patient_age',
                  'case_patient_sex','case_patient_address','case_patient_city','case_patient_state','case_patient_occupation','case_patient_religion','case_patient_economy_status',
                  'category','case_status','case_reviewer','case_listing_status','case_review_status',)
    list_filter = ('case_title','case_patient_name','case_patient_mobile'
                  ,'case_patient_economy_status','case_review_status',)
#CaseHistory admin ends here

#CaseDiagnosis admin starts here
class CaseDiagnosisResource(resources.ModelResource):
    case = fields.Field(column_name=_('Case History'), attribute='case')
    dis = fields.Field(column_name=_('Case Disease'), attribute='dis')
    is_primary= fields.Field(column_name=_('Is Primary'), attribute='is_primary')
    class Meta:
        model = CaseDiagnosis
        fields = ('case','dis','is_primary')
        import_id_fields = fields
        export_order = fields
     
     
class CaseDiagnosisAdmin(ImportExportModelAdmin):
    resource_class = CaseDiagnosisResource
    list_display = ('case','dis','is_primary')
    search_fields = ('case','dis','is_primary')
    list_filter = ('case',)
#CaseDiagnosis admin ends here

#CaseComplaints admin starts here
class CaseComplaintsResource(resources.ModelResource):
    case = fields.Field(column_name=_('Case History'), attribute='case')
    comp_symptoms = fields.Field(column_name=_('Case Symptoms'), attribute='comp_symptoms')
    comp_duration = fields.Field(column_name=_('Complaint Duration'), attribute='comp_duration')
    comp_duration_type = fields.Field(column_name=_('Complaints Duration Type'), attribute='comp_duration_type')
    comp_side = fields.Field(column_name=_('Complaints Side'), attribute='comp_side')
    comp_time = fields.Field(column_name=_('Complaints Time'), attribute='comp_time')
    comp_modality = fields.Field(column_name=_('Complaints Modality'), attribute='comp_modality')
    comp_extension = fields.Field(column_name=_('Complaints Extension'), attribute='comp_extension')
     
    class Meta:
        model = CaseComplaints
        fields = ('case','comp_symptoms','comp_duration','comp_duration_type',
                  'comp_side','comp_time','comp_modality','comp_extension',)
        import_id_fields = fields
        export_order = fields
     
     
class CaseComplaintsAdmin(ImportExportModelAdmin):
    resource_class = CaseComplaintsResource
    list_display = ('case','comp_symptoms','comp_duration','comp_duration_type',
                  'comp_side','comp_time','comp_modality','comp_extension',)
    search_fields = ('case','comp_symptoms','comp_duration','comp_duration_type',
                  'comp_side','comp_time','comp_modality','comp_extension',)
    list_filter = ('case','comp_symptoms',)
#CaseComplaints admin ends here

#CasePersonalHistory admin starts here
class CasePersonalHistoryResource(resources.ModelResource):
    case = fields.Field(column_name=_('Case History'), attribute='case')
    hab = fields.Field(column_name=_('Habit'), attribute='hab')
    phis_duration = fields.Field(column_name=_('Physical Duration'), attribute='phis_duration')
    phis_hab_value = fields.Field(column_name=_('Physical Habit Value'), attribute='phis_hab_value')
    phis_duration_type = fields.Field(column_name=_('Physical Duration Type'), attribute='phis_duration_type')
    phis_consumption_pattern = fields.Field(column_name=_('Consumption Pattern'), attribute='phis_consumption_pattern')
     
    class Meta:
        model = CasePersonalHistory
        fields = ('case','hab','phis_duration','phis_hab_value',
                  'phis_duration_type','phis_consumption_pattern',)
        import_id_fields = fields
        export_order = fields
     
     
class CasePersonalHistoryAdmin(ImportExportModelAdmin):
    resource_class = CasePersonalHistoryResource
    list_display = ('case','hab','phis_duration','phis_hab_value',
                  'phis_duration_type','phis_consumption_pattern',)
    search_fields = ('case','hab','phis_duration','phis_hab_value',
                  'phis_duration_type','phis_consumption_pattern',)
    list_filter = ('case','hab',)
#CasePersonalHistory admin ends here

#CasePhysicalGeneral admin starts here
class CasePhysicalGeneralResource(resources.ModelResource):
    case = fields.Field(column_name=_('Case History'), attribute='case')
    hab = fields.Field(column_name=_('Habit'), attribute='hab')
    phygen_value = fields.Field(column_name=_('Physical General Value'), attribute='phygen_value')
     
    class Meta:
        model = CasePhysicalGeneral
        fields = ('case','hab','phygen_value',)
        import_id_fields = fields
        export_order = fields
     
     
class CasePhysicalGeneralAdmin(ImportExportModelAdmin):
    resource_class = CasePhysicalGeneralResource
    list_display = ('case','hab','phygen_value',)
    search_fields = ('case','hab','phygen_value',)
    list_filter = ('case','hab',)
#CasePhysicalGeneral admin ends here

#CaseMentalGeneral admin starts here
class CaseMentalGeneralResource(resources.ModelResource):
    case = fields.Field(column_name=_('Case History'), attribute='case')
    ment_gen_value = fields.Field(column_name=_('Mental General Value'), attribute='ment_gen_value')
     
    class Meta:
        model = CaseMentalGeneral
        fields = ('case','ment_gen_value',)
        import_id_fields = fields
        export_order = fields
     
     
class CaseMentalGeneralAdmin(ImportExportModelAdmin):
    resource_class = CaseMentalGeneralResource
    list_display = ('case','ment_gen_value',)
    search_fields = ('case','ment_gen_value',)
    list_filter = ('ment_gen_value',)
#CaseMentalGeneral admin ends here

#CasePastHistoryDisease admin starts here
class CasePastHistoryDiseaseResource(resources.ModelResource):
    case = fields.Field(column_name=_('Case History'), attribute='case')
    dis = fields.Field(column_name=_('Disease Name '), attribute='dis')
    his_dis_yronset = fields.Field(column_name=_('Disease Yronset'), attribute='his_dis_yronset')
    his_dis_ageonset = fields.Field(column_name=_('Disease Age of Onset'), attribute='his_dis_ageonset')
    his_dis_trthistory = fields.Field(column_name=_('Disease Trthistory'), attribute='his_dis_trthistory')
    his_dis_outcome = fields.Field(column_name=_('Disease Outcome'), attribute='his_dis_outcome')
     
    class Meta:
        model = CasePastHistoryDisease
        fields = ('case','dis','his_dis_yronset','his_dis_ageonset','his_dis_trthistory','his_dis_outcome',)
        import_id_fields = fields
        export_order = fields
     
     
class CasePastHistoryDiseaseAdmin(ImportExportModelAdmin):
    resource_class = CasePastHistoryDiseaseResource
    list_display = ('case','dis','his_dis_yronset','his_dis_ageonset','his_dis_trthistory','his_dis_outcome',)
    search_fields = ('case','dis','his_dis_yronset','his_dis_ageonset','his_dis_trthistory','his_dis_outcome',)
    list_filter = ('case','dis',)
#CasePastHistoryDisease admin ends here

#CasePastHistory admin starts here
class CasePastHistoryResource(resources.ModelResource):
    case = fields.Field(column_name=_('Case History'), attribute='case')
    his_mas = fields.Field(column_name=_('Past History'), attribute='his_mas')
    phist_value = fields.Field(column_name=_('Physical Value'), attribute='phist_value')
     
    class Meta:
        model = CasePastHistory
        fields = ('case','his_mas','phist_value',)
        import_id_fields = fields
        export_order = fields
     
     
class CasePastHistoryAdmin(ImportExportModelAdmin):
    resource_class = CasePastHistoryResource
    list_display = ('case','his_mas','phist_value',)
    search_fields = ('case','his_mas','phist_value',)
    list_filter= ('phist_value',)
#CasePastHistory admin ends here

#CaseFamilyHistory admin starts here
class CaseFamilyHistoryResource(resources.ModelResource):
    case = fields.Field(column_name=_('Case History'), attribute='case')
    famil_his_alive_dead = fields.Field(column_name=_('Alive Or Dead'), attribute='famil_his_alive_dead')
    famil_his_relation = fields.Field(column_name=_('Family Relation'), attribute='famil_his_relation')
    dis = fields.Field(column_name=_('Case Disease'), attribute='dis')
     
    class Meta:
        model = CaseFamilyHistory
        fields = ('case','famil_his_alive_dead','famil_his_relation','dis',)
        import_id_fields = fields
        export_order = fields
     
     
class CaseFamilyHistoryAdmin(ImportExportModelAdmin):
    resource_class = CaseFamilyHistoryResource
    list_display = ('case','famil_his_alive_dead','famil_his_relation','dis',)
    search_fields = ('case','famil_his_alive_dead','famil_his_relation','dis',)
    list_filter = ('famil_his_alive_dead','dis',)
#CaseFamilyHistory admin ends here

#GynaecologicalHistory admin starts here
class GynaecologicalHistoryResource(resources.ModelResource):
    case = fields.Field(column_name=_('Case History'), attribute='case')
    menarche_date_age = fields.Field(column_name=_('Menarche Date Age'), attribute='menarche_date_age')
    menst_lmp = fields.Field(column_name=_('Last Menstrual Period'), attribute='menst_lmp')
    menst_cycle = fields.Field(column_name=_('Menstrual Cycle'), attribute='menst_cycle')
    menst_duration = fields.Field(column_name=_('Menstrual Duration'), attribute='menst_duration')
    menst_quantity = fields.Field(column_name=_('Menstrual Quantity'), attribute='menst_quantity')
    menst_colour = fields.Field(column_name=_('Menstrual Colour'), attribute='menst_colour')
    menst_odur = fields.Field(column_name=_('Menstrual Odour'), attribute='menst_odur')
    menst_character = fields.Field(column_name=_('Menstrual Character'), attribute='menst_character')
    menst_complaints_b_d_a_menses = fields.Field(column_name=_('Menstrual Complaints B D A Menses'), attribute='menst_complaints_b_d_a_menses')
    menst_leucorrhea = fields.Field(column_name=_('Menstrual Leucorrhea'), attribute='menst_leucorrhea')
    menst_surgery = fields.Field(column_name=_('Menstrual Surgery'), attribute='menst_surgery')
     
    class Meta:
        model = GynaecologicalHistory
        fields = ('case','menarche_date_age','menst_lmp','menst_cycle',
                  'menst_duration','menst_quantity','menst_colour','menst_odur',
                  'menst_character','menst_complaints_b_d_a_menses','menst_leucorrhea','menst_surgery',)
        import_id_fields = fields
        export_order = fields
     
     
class GynaecologicalHistoryAdmin(ImportExportModelAdmin):
    resource_class = GynaecologicalHistoryResource
    list_display = ('case','menarche_date_age','menst_lmp','menst_cycle',
                  'menst_duration','menst_quantity','menst_colour','menst_odur',
                  'menst_character','menst_complaints_b_d_a_menses','menst_leucorrhea','menst_surgery',)
    search_fields = ('case','menarche_date_age','menst_lmp','menst_cycle',
                  'menst_duration','menst_quantity','menst_colour','menst_odur',
                  'menst_character','menst_complaints_b_d_a_menses','menst_leucorrhea','menst_surgery',)
    list_filter = ('case','menarche_date_age','menst_surgery',)
#GynaecologicalHistory admin ends here

#CaseObstrericHistory admin starts here
class CaseObstrericHistoryResource(resources.ModelResource):
    case = fields.Field(column_name=_('Case History'), attribute='case')
    pbh_his_gravida = fields.Field(column_name=_('Pbh Gravida Histroy'), attribute='pbh_his_gravida')
    pbh_his_para = fields.Field(column_name=_('Pbh Para History'), attribute='pbh_his_para')
    pbh_his_abortion = fields.Field(column_name=_('Pbh Abortion History'), attribute='pbh_his_abortion')
    pbh_his_stillbirth = fields.Field(column_name=_('Pbh Stillbirth History'), attribute='pbh_his_stillbirth')
    pbh_his_living = fields.Field(column_name=_('Pbh Living History'), attribute='pbh_his_living')
    pbh_his_period_of_pregnancy = fields.Field(column_name=_('Pbh Pregnancy Histroy'), attribute='pbh_his_period_of_pregnancy')
    pbh_his_lactation_history = fields.Field(column_name=_('Pbh Lactation History'), attribute='pbh_his_lactation_history')
    pbh_his_comp_dur_pregnancy = fields.Field(column_name=_('Pbh Complaints During Pregnancy History'), attribute='pbh_his_comp_dur_pregnancy')
    pbh_his_nature_of_labor = fields.Field(column_name=_('Pbh Nature of Labour History'), attribute='pbh_his_nature_of_labor')
    pbh_his_nature_of_delivery = fields.Field(column_name=_('Pbh Nature of Delivery History'), attribute='pbh_his_nature_of_delivery')
    pbh_his_nature_of_puerperium = fields.Field(column_name=_('Pbh Nature of Puerperium History'), attribute='pbh_his_nature_of_puerperium')
     
    class Meta:
        model = CaseObstrericHistory
        fields = ('case','pbh_his_gravida','pbh_his_para','pbh_his_abortion',
                  'pbh_his_stillbirth','pbh_his_living','pbh_his_period_of_pregnancy','pbh_his_lactation_history',
                  'pbh_his_comp_dur_pregnancy','pbh_his_nature_of_labor','pbh_his_nature_of_delivery','pbh_his_nature_of_puerperium',)
        import_id_fields = fields
        export_order = fields
     
     
class CaseObstrericHistoryAdmin(ImportExportModelAdmin):
    resource_class = CaseObstrericHistoryResource
    list_display = ('case','pbh_his_gravida','pbh_his_para','pbh_his_abortion',
                  'pbh_his_stillbirth','pbh_his_living','pbh_his_period_of_pregnancy','pbh_his_lactation_history',
                  'pbh_his_comp_dur_pregnancy','pbh_his_nature_of_labor','pbh_his_nature_of_delivery','pbh_his_nature_of_puerperium',)
    search_fields = ('case','pbh_his_gravida','pbh_his_para','pbh_his_abortion',
                  'pbh_his_stillbirth','pbh_his_living','pbh_his_period_of_pregnancy','pbh_his_lactation_history',
                  'pbh_his_comp_dur_pregnancy','pbh_his_nature_of_labor','pbh_his_nature_of_delivery','pbh_his_nature_of_puerperium',)
    list_filter = ('case','pbh_his_gravida','pbh_his_para','pbh_his_abortion',)
#CaseObstrericHistory admin ends here

#CaseObstrericChildHistory admin starts here
class CaseObstrericChildHistoryResource(resources.ModelResource):
    case = fields.Field(column_name=_('Case History'), attribute='case')
    chd_his_child = fields.Field(column_name=_('Child History'), attribute='chd_his_child')
    chd_his_alive = fields.Field(column_name=_('Is Alive'), attribute='chd_his_alive')
    chd_his_causeofdeath = fields.Field(column_name=_('Cause of Death'), attribute='chd_his_causeofdeath')
    chd_his_birthweight = fields.Field(column_name=_('Birth Weight'), attribute='chd_his_birthweight')
     
    class Meta:
        model = CaseObstrericChildHistory
        fields = ('case','chd_his_child','chd_his_alive','chd_his_causeofdeath','chd_his_birthweight',)
        import_id_fields = fields
        export_order = fields
     
     
class CaseObstrericChildHistoryAdmin(ImportExportModelAdmin):
    resource_class = CaseObstrericChildHistoryResource
    list_display = ('case','chd_his_child','chd_his_alive','chd_his_causeofdeath','chd_his_birthweight',)
    search_fields = ('case','chd_his_child','chd_his_alive','chd_his_causeofdeath','chd_his_birthweight',)
    list_filter = ('case','chd_his_causeofdeath',)
#CaseObstrericChildHistory admin ends here

#CasePhysicalFindings admin starts here
class CasePhysicalFindingsResource(resources.ModelResource):
    case = fields.Field(column_name=_('Case History'), attribute='case')
    fin_mas = fields.Field(column_name=_('Physical Finding'), attribute='fin_mas')
    phyfind_value = fields.Field(column_name=_('Physical Finding Value'), attribute='phyfind_value')
     
    class Meta:
        model = CasePhysicalFindings
        fields = ('case','fin_mas','phyfind_value',)
        import_id_fields = fields
        export_order = fields
     
     
class CasePhysicalFindingsAdmin(ImportExportModelAdmin):
    resource_class = CasePhysicalFindingsResource
    list_display = ('case','fin_mas','phyfind_value',)
    search_fields = ('case','fin_mas','phyfind_value',)
    list_filter = ('fin_mas','phyfind_value',)
#CasePhysicalFindings admin ends here

#CaseRepertorisation admin starts here
class CaseRepertorisationResource(resources.ModelResource):
    case = fields.Field(column_name=_('Case History'), attribute='case')
    rep_document = fields.Field(column_name=_('Repertorisation  Document'), attribute='rep_document')
    rep_analysis = fields.Field(column_name=_('Repertorisation Analysis'), attribute='rep_analysis')
     
    class Meta:
        model = CaseRepertorisation
        fields = ('case','rep_document','rep_analysis',)
        import_id_fields = fields
        export_order = fields
     
     
class CaseRepertorisationAdmin(ImportExportModelAdmin):
    resource_class = CaseRepertorisationResource
    list_display = ('case','rep_document','rep_analysis',)
    search_fields = ('case','rep_document','rep_analysis',)
    list_filter = ('case','rep_analysis',)
#CaseRepertorisation admin ends here

#CaseMiasamaticAnalysis admin starts here
class CaseMiasamaticAnalysisResource(resources.ModelResource):
    case = fields.Field(column_name=_('Case History'), attribute='case')
    mia_analys_mas = fields.Field(column_name=_('Miasamatic Analysis'), attribute='mia_analys_mas')
    mia_analys_value = fields.Field(column_name=_(' Miasamatic Analysis Value'), attribute='mia_analys_value')
      
    class Meta:
        model = CaseMiasamaticAnalysis
        fields = ('case','mia_analys_mas','mia_analys_value',)
        import_id_fields = fields
        export_order = fields
      
      
class CaseMiasamaticAnalysisAdmin(ImportExportModelAdmin):
    resource_class = CaseMiasamaticAnalysisResource
    list_display = ('case','mia_analys_mas','mia_analys_value',)
    search_fields = ('case','mia_analys_mas','mia_analys_value',)
    list_filter = ('case','mia_analys_mas',)
#CaseMiasamaticAnalysis admin ends here

#CaseMedicineManagement admin starts here
class CaseMedicineManagementResource(resources.ModelResource):
    case = fields.Field(column_name=_('Case History'), attribute='case')
    prescription_date = fields.Field(column_name=_('Prescription Date'), attribute='prescription_date')
    prescription_order = fields.Field(column_name=_('Prescription Order'), attribute='prescription_order')
    prescription_oridl_scale = fields.Field(column_name=_('Prescription ORIDL Scale'), attribute='prescription_oridl_scale')
    outcome_of_prev_presc = fields.Field(column_name=_('Outcome of Previous Prescription'), attribute='outcome_of_prev_presc')
    marks_for_improvement = fields.Field(column_name=_('Marks for Improvement'), attribute='marks_for_improvement')
    
     
    class Meta:
        model = CaseMedicineManagement
        fields = ('case','prescription_date','prescription_order','prescription_oridl_scale','outcome_of_prev_presc','marks_for_improvement',)
        import_id_fields = fields
        export_order = fields
     
     
class CaseMedicineManagementAdmin(ImportExportModelAdmin):
    resource_class = CaseMedicineManagementResource
    list_display = ('case','prescription_date','prescription_order','prescription_oridl_scale','outcome_of_prev_presc','marks_for_improvement',)
    search_fields = ('case','prescription_date','prescription_order','prescription_oridl_scale','outcome_of_prev_presc','marks_for_improvement',)
    list_filter = ('case','prescription_order','marks_for_improvement',)
#CaseMedicineManagement admin ends here

#MedicinePrescriptionMapping admin starts here
class MedicinePrescriptionMappingResource(resources.ModelResource):
    medi_mgnt = fields.Field(column_name=_('Medical Management'), attribute='medi_mgnt')
    prescription = fields.Field(column_name=_('Prescription'), attribute='prescription' )
    potency = fields.Field(column_name=_('Potency'), attribute='potency')
    dosage = fields.Field(column_name=_('Dosage'), attribute='dosage')
    
    class Meta:
        model = MedicinePrescriptionMapping
        fields = ('medi_mgnt','prescription','potency','dosage',)
        import_id_fields = fields
        export_order = fields
     
     
class MedicinePrescriptionMappingAdmin(ImportExportModelAdmin):
    resource_class = MedicinePrescriptionMappingResource
    list_display = ('medi_mgnt','prescription','potency','dosage',)
    search_fields = ('medi_mgnt','prescription','potency','dosage',)
    list_filter = ('medi_mgnt','dosage',)
#MedicinePrescriptionMapping admin ends here

#PrescriptionSymptomMapping admin starts here
class PrescriptionSymptomMappingResource(resources.ModelResource):
    medi_pres_map = fields.Field(column_name=_('Medical Prescription'), attribute='medi_pres_map')
    symptom = fields.Field(column_name=_('Symptoms'), attribute='symptom')
    
    class Meta:
        model = PrescriptionSymptomMapping
        fields = ('medi_pres_map','symptom',)
        import_id_fields = fields
        export_order = fields
     
     
class PrescriptionSymptomMappingAdmin(ImportExportModelAdmin):
    resource_class = PrescriptionSymptomMappingResource
    list_display = ('medi_pres_map','symptom',)
    search_fields = ('medi_pres_map','symptom',)
    list_filter = ('medi_pres_map','symptom',)
#PrescriptionSymptomMapping admin ends here

#CaseAddonTherapy admin starts here
class CaseAddonTherapyResource(resources.ModelResource):
    case = fields.Field(column_name=_('Case History'), attribute='case')
    addon_thrpy_mas = fields.Field(column_name=_('Add-on Therapy'), attribute='addon_thrpy_mas')
    duration_tamper_homeo = fields.Field(column_name=_('Duration Temper Homeo'), attribute='duration_tamper_homeo')
    medicine_name = fields.Field(column_name=_('Medicine Name'), attribute='medicine_name')
    medicine_dosage = fields.Field(column_name=_('Medicine Dosage'), attribute='medicine_dosage')
    
    class Meta:
        model = CaseAddonTherapy
        fields = ('case','addon_thrpy_mas','duration_tamper_homeo','medicine_name','medicine_dosage',)
        import_id_fields = fields
        export_order = fields
     
     
class CaseAddonTherapyAdmin(ImportExportModelAdmin):
    resource_class = CaseAddonTherapyResource
    list_display = ('case','addon_thrpy_mas','duration_tamper_homeo','medicine_name','medicine_dosage',)
    search_fields = ('case','addon_thrpy_mas','duration_tamper_homeo','medicine_name','medicine_dosage',)
    list_filter = ('case','addon_thrpy_mas','medicine_name',)
#CaseAddonTherapy admin ends here

#CaseInvestigation admin starts here
class CaseInvestigationResource(resources.ModelResource):
    case = fields.Field(column_name=_('Case History'), attribute='case')
    investg_mas = fields.Field(column_name=_('Investigation'), attribute='investg_mas')
    investg_value = fields.Field(column_name=_('Investigation Value'), attribute='investg_value')
    investg_file = fields.Field(column_name=_('Investigation File'), attribute='investg_file')
    
    class Meta:
        model = CaseInvestigation
        fields = ('case','investg_mas','investg_value','investg_file',)
        import_id_fields = fields
        export_order = fields
     
     
class CaseInvestigationAdmin(ImportExportModelAdmin):
    resource_class = CaseInvestigationResource
    list_display = ('case','investg_mas','investg_value','investg_file',)
    search_fields = ('case','investg_mas','investg_value','investg_file',)
    list_filter = ('case','investg_value',)
#CaseInvestigation admin ends here

#CaseStatusHistory admin starts here
class CaseStatusHistoryResource(resources.ModelResource):
    case = fields.Field(column_name=_('Case History'), attribute='case')
    case_status = fields.Field(column_name=_('Case Status'), attribute='case_status')
    case_remarks = fields.Field(column_name=_('Case Remarks'), attribute='case_remarks')
    
    class Meta:
        model = CaseStatusHistory
        fields = ('case','case_status','case_remarks',)
        import_id_fields = fields
        export_order = fields
     
     
class CaseStatusHistoryAdmin(ImportExportModelAdmin):
    resource_class = CaseStatusHistoryResource
    list_display = ('case','case_status','case_remarks',)
    search_fields = ('case','case_status','case_remarks',)
    list_filter = ('case_remarks',)
#CaseStatusHistory admin ends here

#CaseReviewStatusHistory admin starts here
class CaseReviewStatusHistoryResource(resources.ModelResource):
    case = fields.Field(column_name=_('Case History'), attribute='case')
    case_review_status = fields.Field(column_name=_('Case Review Status'), attribute='case_review_status')
    case_review_remarks = fields.Field(column_name=_('Case Review Remarks'), attribute='case_review_remarks')
    
    class Meta:
        model = CaseReviewStatusHistory
        fields = ('case','case_review_status','case_review_remarks',)
        import_id_fields = fields
        export_order = fields
     
     
class CaseReviewStatusHistoryAdmin(ImportExportModelAdmin):
    resource_class = CaseReviewStatusHistoryResource
    list_display = ('case','case_review_status','case_review_remarks',)
    search_fields = ('case','case_review_status','case_review_remarks',)
    list_filter = ('case_review_status',)
#CaseReviewStatusHistory admin ends here

#CaseChecklistMapping admin starts here
class CaseChecklistMappingResource(resources.ModelResource):
    case = fields.Field(column_name=_('Case History'), attribute='case')
    checklist = fields.Field(column_name=_('Case CheckList'), attribute='checklist')
    checklist_value = fields.Field(column_name=_('Checklist Value'), attribute='checklist_value')
    
    class Meta:
        model = CaseChecklistMapping
        fields = ('case','checklist','checklist_value',)
        import_id_fields = fields
        export_order = fields
     
     
class CaseChecklistMappingAdmin(ImportExportModelAdmin):
    resource_class = CaseChecklistMappingResource
    list_display = ('case','checklist','checklist_value',)
    search_fields = ('case','checklist','checklist_value',)
    list_filter = ('checklist_value',)
#CaseChecklistMapping admin ends here



admin.site.register(CaseCategory, CaseCategoryAdmin)
admin.site.register(CaseStatus, CaseStatusAdmin)
admin.site.register(CaseReviewStatus, CaseReviewStatusAdmin)
admin.site.register(CaseListingStatus, CaseListingStatusAdmin)
admin.site.register(CaseCheckListMaster, CaseCheckListMasterAdmin)
admin.site.register(CaseHistory, CaseHistoryAdmin)
admin.site.register(CaseDiagnosis, CaseDiagnosisAdmin)
admin.site.register(CaseComplaints, CaseComplaintsAdmin)
admin.site.register(CasePersonalHistory, CasePersonalHistoryAdmin)
admin.site.register(CasePhysicalGeneral, CasePhysicalGeneralAdmin)
admin.site.register(CaseMentalGeneral, CaseMentalGeneralAdmin)
admin.site.register(CasePastHistoryDisease, CasePastHistoryDiseaseAdmin)
admin.site.register(CasePastHistory, CasePastHistoryAdmin)
admin.site.register(CaseFamilyHistory, CaseFamilyHistoryAdmin)
admin.site.register(GynaecologicalHistory, GynaecologicalHistoryAdmin)
admin.site.register(CaseObstrericHistory, CaseObstrericHistoryAdmin)
admin.site.register(CaseObstrericChildHistory, CaseObstrericChildHistoryAdmin)
admin.site.register(CasePhysicalFindings, CasePhysicalFindingsAdmin)
admin.site.register(CaseRepertorisation, CaseRepertorisationAdmin)
admin.site.register(CaseMiasamaticAnalysis, CaseMiasamaticAnalysisAdmin)
admin.site.register(CaseMedicineManagement, CaseMedicineManagementAdmin)
admin.site.register(MedicinePrescriptionMapping, MedicinePrescriptionMappingAdmin)
admin.site.register(PrescriptionSymptomMapping, PrescriptionSymptomMappingAdmin)
admin.site.register(CaseAddonTherapy, CaseAddonTherapyAdmin)
admin.site.register(CaseInvestigation, CaseInvestigationAdmin)
admin.site.register(CaseStatusHistory, CaseStatusHistoryAdmin)
admin.site.register(CaseReviewStatusHistory, CaseReviewStatusHistoryAdmin)
admin.site.register(CaseChecklistMapping, CaseChecklistMappingAdmin)


