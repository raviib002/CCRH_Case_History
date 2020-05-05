"""
Project    : "CCRH"
module     : master/admin
created    : 03/03/2020
Author     : Manish Kumar
"""

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from master.models import (State,PhysicalFindingMaster,
                           City,HabitMaster,PhysicalGeneralType,PhysicalGeneralMaster,
                            Status,DiseaseMaster,InvestigationsMaster,PastHistoryMaster,
                            MiasamaticAnalysisMaster,ClinicalSetting,SymptomsMaster,PastHistoryType,PhysicalFindingType,
                            MedicineType,MedicineMaster,PhysicalFindingMeasurementMaster,AddonTherapyMaster
                           )
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget, DateTimeWidget, IntegerWidget
from import_export.admin import ImportMixin, ExportMixin, ImportExportMixin
from import_export.formats import base_formats
from django.forms import forms, ModelForm, Select
from import_export import resources, fields

# Register your models here.

#status admin starts here    
class StatusResource(resources.ModelResource):
    status_name = fields.Field(column_name=_('Status name'), attribute='status_name')
    
    class Meta:
        model = Status
        fields = ('status_name', )
        import_id_fields = fields
        export_order = fields
    
class StatusAdmin(ImportExportModelAdmin):
    resource_class = StatusResource
    list_display = ('status_name', )
    search_fields = ('status_name',)
#Status admin ends here

#State admin starts here    
class StateResource(resources.ModelResource):
    state_name = fields.Field(column_name=_('State name'), attribute='state_name')
    country_id = fields.Field(column_name=_('Country Id'), attribute='country_id',)
    status = fields.Field(column_name=_('Status'), attribute='status', widget=ForeignKeyWidget(Status, 'status_name'))
    
    class Meta:
        model = State
        fields = ('state_name','country_id','status', )
        import_id_fields = fields
        export_order = fields
    
class StateAdmin(ImportExportModelAdmin):
    resource_class = StateResource
    list_display = ('state_name','country_id','status', )
    search_fields = ('state_name','')
#State admin ends here
    
#City admin starts here    
class CityResource(resources.ModelResource):
    city_name = fields.Field(column_name=_('City name'), attribute='city_name')
    state = fields.Field(column_name=_('State'), attribute='state', widget=ForeignKeyWidget(State, 'state_name'))
    status = fields.Field(column_name=_('Status'), attribute='status', widget=ForeignKeyWidget(Status, 'status_name'))
    
    class Meta:
        model = City
        fields = ('city_name', 'state', 'status')
        import_id_fields = fields
        export_order = fields
    
class CityAdmin(ImportExportModelAdmin):
    resource_class = CityResource
    list_display = ('city_name','state','status', )
    search_fields = ('city_name',)
#City admin ends here    

#clinical Setting Admin starts here
class ClinicalsettingResource(resources.ModelResource):
    cs_name = fields.Field(column_name=_('Clinical Setting Name'), attribute='cs_name')
    status = fields.Field(column_name=_('Status'), attribute='status', widget=ForeignKeyWidget(Status, 'status_name'))
    
    class Meta:
        model = ClinicalSetting
        fields = ('cs_name', 'status',)
        import_id_fields = fields
        export_order = fields
    
class ClinicalsettingAdmin(ImportExportModelAdmin):
    resource_class = ClinicalsettingResource
    list_display = ('cs_name','status', )
    search_fields = ('cs_name',)
#clinical Setting Admin ends here

#Medicine Type admin starts here    
class MedicineTypeResource(resources.ModelResource):
    med_type = fields.Field(column_name=_('Medicine Type'), attribute='med_type')
    status = fields.Field(column_name=_('Status'), attribute='status', widget=ForeignKeyWidget(Status, 'status_name'))
    
    class Meta:
        model = MedicineType
        fields = ('med_type', 'status',)
        import_id_fields = fields
        export_order = fields
    
class MedicineTypeAdmin(ImportExportModelAdmin):
    resource_class = MedicineTypeResource
    list_display = ('med_type','status', )
    search_fields = ('med_type',)
#Medicine Type admin ends here 
   
#Medicine Master  Admin starts here
class MedicineMasterResource(resources.ModelResource):
    med_name = fields.Field(column_name=_('Medicine Name'), attribute='med_name')
    med_type = fields.Field(column_name=_('Medicine Type'), attribute='med_type', widget=ForeignKeyWidget(MedicineType, 'med_type'))
    mother_tincture = fields.Field(column_name=_('Medicine Tincture'), attribute='mother_tincture')
    potency_3x6x = fields.Field(column_name=_('Potency 3x6x'), attribute='potency_3x6x')
    potency_6 = fields.Field(column_name=_('Potency 6'), attribute='potency_6')
    potency_30 = fields.Field(column_name=_('Potency 30'), attribute='potency_30')
    potency_200 = fields.Field(column_name=_('Potency 200'), attribute='potency_200')
    potency_1m = fields.Field(column_name=_('Potency 1m'), attribute='potency_1m')
    status = fields.Field(column_name=_('Status'), attribute='status', widget=ForeignKeyWidget(Status, 'status_name'))
    
    class Meta:
        model = MedicineMaster
        fields = ('med_name','med_type','mother_tincture','potency_3x6x','potency_6','potency_30','potency_200','potency_1m', 'status',)
        import_id_fields = fields
        export_order = fields
    
class MedicineMasterAdmin(ImportExportModelAdmin):
    resource_class = MedicineMasterResource
    list_display =  ('med_name','med_type','mother_tincture','potency_3x6x','potency_6','potency_30','potency_200','potency_1m', 'status',)
    search_fields = ('med_type','med_name',)
#Medicine Master  Admin ends here    

#Symptoms admin starts here    
class SymptomsMasterResource(resources.ModelResource):
    sym_name = fields.Field(column_name=_('Symptoms Name'), attribute='sym_name')
    sym_desc = fields.Field(column_name=_('Symptoms Description'), attribute='sym_desc')
    status = fields.Field(column_name=_('Status'), attribute='status', widget=ForeignKeyWidget(Status, 'status_name'))
    
    class Meta:
        model = SymptomsMaster
        fields = ('sym_name','sym_desc','status',)
        import_id_fields = fields
        export_order = fields
    
class SymptomsMasterAdmin(ImportExportModelAdmin):
    resource_class = SymptomsMasterResource
    list_display =  ('sym_name','sym_desc','status',)
    search_fields = ('med_type',)
#Symptoms admin ends here

#Disease admin starts here    
class DiseaseMasterResource(resources.ModelResource):
    dis_name = fields.Field(column_name=_('Disease Name'), attribute='dis_name')
    dis_desc = fields.Field(column_name=_('Disease Description'), attribute='dis_desc')
    dis_icd_code = fields.Field(column_name=_('Disease ICD Code'), attribute='dis_icd_code')
    status = fields.Field(column_name=_('Status'), attribute='status', widget=ForeignKeyWidget(Status, 'status_name'))
    
    class Meta:
        model = DiseaseMaster
        fields = ('dis_name','dis_desc','dis_icd_code','status',)
        import_id_fields = fields
        export_order = fields
    
class DiseaseMasterAdmin(ImportExportModelAdmin):
    resource_class = DiseaseMasterResource
    list_display =  ('dis_name','dis_desc','dis_icd_code','status',)
    search_fields = ('dis_name',)
#Disease admin ends here

#Investigation admin starts here    
class InvestigationsMasterResource(resources.ModelResource):
    investg_name = fields.Field(column_name=_('Investigation Name'), attribute='investg_name')
    investg_desc = fields.Field(column_name=_('Investigation Description'), attribute='investg_desc')
    status = fields.Field(column_name=_('Status'), attribute='status', widget=ForeignKeyWidget(Status, 'status_name'))
    
    class Meta:
        model = InvestigationsMaster
        fields = ('investg_name','investg_desc','status',)
        import_id_fields = fields
        export_order = fields
    
class InvestigationsMasterAdmin(ImportExportModelAdmin):
    resource_class = InvestigationsMasterResource
    list_display =  ('investg_name','investg_desc','status',)
    search_fields = ('investg_name',)
#Investigation admin ends here 

#Habit admin starts here    
class HabitMasterResource(resources.ModelResource):
    hab_name = fields.Field(column_name=_('Habit Name'), attribute='hab_name')
    hab_type = fields.Field(column_name=_('Habit Type'), attribute='hab_type')
    status = fields.Field(column_name=_('Status'), attribute='status', widget=ForeignKeyWidget(Status, 'status_name'))
    
    class Meta:
        model = HabitMaster
        fields = ('hab_name','hab_type','status',)
        import_id_fields = fields
        export_order = fields
    
class HabitMasterAdmin(ImportExportModelAdmin):
    resource_class = HabitMasterResource
    list_display =  ('hab_name','hab_type','status',)
    search_fields = ('hab_name',)
#Habit admin ends here    
 
#Physical General admin starts here    
class PhysicalGeneralTypeResource(resources.ModelResource):
    gen_type_name = fields.Field(column_name=_('Physical General Type Name'), attribute='gen_type_name')
    status = fields.Field(column_name=_('Status'), attribute='status', widget=ForeignKeyWidget(Status, 'status_name'))
    
    class Meta:
        model = PhysicalGeneralType
        fields = ('gen_type_name','status',)
        import_id_fields = fields
        export_order = fields
    
class PhysicalGeneralTypeAdmin(ImportExportModelAdmin):
    resource_class = PhysicalGeneralTypeResource
    list_display =  ('gen_type_name','status',)
    search_fields = ('gen_type_name',)
#Physical General admin ends here    

#Physical General Master admin starts here    
class PhysicalGeneralMasterResource(resources.ModelResource):
    gen_type = fields.Field(column_name=_('Physical General Type'), attribute='gen_type', widget=ForeignKeyWidget(PhysicalGeneralType, 'gen_type'))
    gen_name = fields.Field(column_name=_('Physical General Name'), attribute='gen_name')
    gen_value_type = fields.Field(column_name=_('Physical General Type'), attribute='gen_value_type')
    status = fields.Field(column_name=_('Status'), attribute='status', widget=ForeignKeyWidget(Status, 'status_name'))
    
    class Meta:
        model = PhysicalGeneralMaster
        fields = ('gen_type','gen_name','gen_value_type','status',)
        import_id_fields = fields
        export_order = fields
    
class PhysicalGeneralMasterAdmin(ImportExportModelAdmin):
    resource_class = PhysicalGeneralMasterResource
    list_display =  ('gen_type','gen_name','gen_value_type','status',)
    search_fields = ('gen_name',)
#Physical General Master admin ends here    

# Past History admin starts here    
class PastHistoryTypeResource(resources.ModelResource):
    his_type_name = fields.Field(column_name=_('History Type Name'), attribute='his_type_name')
    status = fields.Field(column_name=_('Status'), attribute='status', widget=ForeignKeyWidget(Status, 'status_name'))
    class Meta:
        model = PastHistoryType
        fields = ('his_type_name','status',)
        import_id_fields = fields
        export_order = fields
    
class PastHistoryTypeAdmin(ImportExportModelAdmin):
    resource_class = PastHistoryTypeResource
    list_display =  ('his_type_name','status',)
    search_fields = ('his_type_name',)
# Past History admin ends here 

# Past History Master admin starts here    
class PastHistoryMasterResource(resources.ModelResource):
    his_type = fields.Field(column_name=_('Hospital Type'), attribute='his_type', widget=ForeignKeyWidget(PastHistoryType, 'his_type'))
    his_name = fields.Field(column_name=_('Hospital Name'), attribute='his_name')
    status = fields.Field(column_name=_('Status'), attribute='status', widget=ForeignKeyWidget(Status, 'status_name'))
    
    class Meta:
        model = PastHistoryMaster
        fields = ('his_type','his_name','status',)
        import_id_fields = fields
        export_order = fields
    
class PastHistoryMasterAdmin(ImportExportModelAdmin):
    resource_class = PastHistoryMasterResource
    list_display =  ('his_type','his_name','status',)
    search_fields = ('his_name',)
# Past History Master admin ends here

#Physical Finding Type admin starts here    
class PhysicalFindingTypeResource(resources.ModelResource):
    find_type = fields.Field(column_name=_('Physical Finding Type Name'), attribute='find_type')
    status = fields.Field(column_name=_('Status'), attribute='status', widget=ForeignKeyWidget(Status, 'status_name'))
    
    class Meta:
        model = PhysicalFindingType
        fields = ('find_type','status',)
        import_id_fields = fields
        export_order = fields
    
class PhysicalFindingTypeAdmin(ImportExportModelAdmin):
    resource_class = PhysicalFindingTypeResource
    list_display =  ('find_type','status',)
    search_fields = ('find_type',)
#Physical Finding Type admin ends here   
  
#Physical Finding Measurement admin starts here    
class PhysicalFindingMeasurementMasterResource(resources.ModelResource):
    measurement = fields.Field(column_name=_('Physical Finding Measurement'), attribute='measurement')
    status = fields.Field(column_name=_('Status'), attribute='status', widget=ForeignKeyWidget(Status, 'status_name'))
    
    class Meta:
        model = PhysicalFindingMeasurementMaster
        fields = ('measurement','status',)
        import_id_fields = fields
        export_order = fields
    
class PhysicalFindingMeasurementMasterAdmin(ImportExportModelAdmin):
    resource_class = PhysicalFindingMeasurementMasterResource
    list_display =  ('measurement','status',)
    search_fields = ('measurement',)
#Physical Finding Measurement admin ends here 
  
#Physical Finding Master admin starts here    
class PhysicalFindingMasterResource(resources.ModelResource):
    fin_type = fields.Field(column_name=_('Physical Finding Type'), attribute='fin_type', widget=ForeignKeyWidget(PhysicalFindingType, 'fin_type'))
    find_name = fields.Field(column_name=_('Physical Find Name'), attribute='find_name')
    measure = fields.Field(column_name=_('Measurement'), attribute='measure', widget=ForeignKeyWidget(PhysicalFindingMeasurementMaster, 'measure'))
    status = fields.Field(column_name=_('Status'), attribute='status', widget=ForeignKeyWidget(Status, 'status_name'))
    
    class Meta:
        model = PhysicalFindingMaster
        fields = ('fin_type','find_name','measure','status',)
        import_id_fields = fields
        export_order = fields
    
class PhysicalFindingMasterAdmin(ImportExportModelAdmin):
    resource_class = PhysicalFindingMasterResource
    list_display =  ('fin_type','find_name','measure','status',)
    search_fields = ('find_name',)
#Physical Finding Master admin ends here 

#Miasamatic Analysis admin starts here    
class MiasamaticAnalysisMasterResource(resources.ModelResource):
    mia_analys_name = fields.Field(column_name=_('Miasamatic Name'), attribute='mia_analys_name')
    status = fields.Field(column_name=_('Status'), attribute='status', widget=ForeignKeyWidget(Status, 'status_name'))
     
    class Meta:
        model = MiasamaticAnalysisMaster
        fields = ('mia_analys_name','status',)
        import_id_fields = fields
        export_order = fields
     
class MiasamaticAnalysisMasterAdmin(ImportExportModelAdmin):
    resource_class = MiasamaticAnalysisMasterResource
    list_display =  ('mia_analys_name','status',)
    search_fields = ('mia_analys_name',)
#Miasamatic Analysis admin ends here

# Addon Therapy admin starts here    
class AddonTherapyMasterResource(resources.ModelResource):
    thrpy_name = fields.Field(column_name=_('Therapy Name'), attribute='thrpy_name')
    status = fields.Field(column_name=_('Status'), attribute='status', widget=ForeignKeyWidget(Status, 'status_name'))
    
    class Meta:
        model = AddonTherapyMaster
        fields = ('thrpy_name','status',)
        import_id_fields = fields
        export_order = fields
    
class AddonTherapyMasterAdmin(ImportExportModelAdmin):
    resource_class = AddonTherapyMasterResource
    list_display =  ('thrpy_name','status',)
    search_fields = ('thrpy_name',)
# Addon Therapy admin ends here 


# admin.site.register(Status, StatusAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(ClinicalSetting, ClinicalsettingAdmin)
admin.site.register(MedicineType, MedicineTypeAdmin)
admin.site.register(MedicineMaster, MedicineMasterAdmin)
admin.site.register(SymptomsMaster, SymptomsMasterAdmin)
admin.site.register(DiseaseMaster, DiseaseMasterAdmin)
admin.site.register(InvestigationsMaster, InvestigationsMasterAdmin)
admin.site.register(HabitMaster, HabitMasterAdmin)
admin.site.register(PhysicalGeneralType, PhysicalGeneralTypeAdmin)
admin.site.register(PhysicalGeneralMaster, PhysicalGeneralMasterAdmin)
admin.site.register(PastHistoryType, PastHistoryTypeAdmin)
admin.site.register(PastHistoryMaster, PastHistoryMasterAdmin)
admin.site.register(PhysicalFindingType, PhysicalFindingTypeAdmin)
admin.site.register(PhysicalFindingMeasurementMaster, PhysicalFindingMeasurementMasterAdmin)
admin.site.register(PhysicalFindingMaster, PhysicalFindingMasterAdmin)
admin.site.register(MiasamaticAnalysisMaster, MiasamaticAnalysisMasterAdmin)
admin.site.register(AddonTherapyMaster, AddonTherapyMasterAdmin)