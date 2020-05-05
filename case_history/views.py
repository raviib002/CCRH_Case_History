from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls.base import reverse_lazy
import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

""" Dashboard functionality  - Starts"""
@login_required
def dashboard(request):
    if request.method == "GET":
        data_list = [{'case_id':'HCCR0101','case_name':'Chronical Patient','patient_name':'Ramadhir Singh','doctor_name':'Ramakant Acharya','doctor_reg_no':'DD000001','disease':'Typhoid','medicine':'DCold','symptoms':'Internal Fever','status':'Accepted'},
                     {'case_id':'HCCR0102','case_name':'Hereditary Patient','patient_name':'Gajendra Singh','doctor_name':'Debashis Panda','doctor_reg_no':'DD000002','disease':'Malaria','medicine':'HCQ','symptoms':'Shivering','status':'Not Accepted'},
                     {'case_id':'HCCR0103','case_name':'Genetic Patient','patient_name':'Yuvraj Singh','doctor_name':'Ramakant Acharya','doctor_reg_no':'DD000003','disease':'Dengue','medicine':'Betadin','symptoms':'Headache','status':'Under Review'},
                     {'case_id':'HCCR0104','case_name':'Genetic Patient','patient_name':'Mahendra Singh','doctor_name':'Umakant Lall','doctor_reg_no':'DD000004','disease':'COVID-19','medicine':'HCQ','symptoms':'Respiratory Problem','status':'Not Accepted'},
                     {'case_id':'HCCR0105','case_name':'Hereditary Patient','patient_name':'Nagendra Singh','doctor_name':'Dr Shalunke','doctor_reg_no':'DD000005','disease':'Filaria','medicine':'FerroMagnus','symptoms':'Swelling','status':'Under Review'},
                     {'case_id':'HCCR0106','case_name':'Chronical Patient','patient_name':'Narendra Singh','doctor_name':'Debashis Panda','doctor_reg_no':'DD000006','disease':'Cardiac Arrest','medicine':'Sorbitet','symptoms':'Chest Burn','status':'Accepted'},
                     {'case_id':'HCCR0106','case_name':'Chronical Patient','patient_name':'Narendra Singh','doctor_name':'Debashis Panda','doctor_reg_no':'DD000006','disease':'Cardiac Arrest','medicine':'Sorbitet','symptoms':'Chest Burn','status':'Accepted'},
                     {'case_id':'HCCR0106','case_name':'Chronical Patient','patient_name':'Narendra Singh','doctor_name':'Debashis Panda','doctor_reg_no':'DD000006','disease':'Cardiac Arrest','medicine':'Sorbitet','symptoms':'Chest Burn','status':'Accepted'},
                     {'case_id':'HCCR0106','case_name':'Chronical Patient','patient_name':'Narendra Singh','doctor_name':'Debashis Panda','doctor_reg_no':'DD000006','disease':'Cardiac Arrest','medicine':'Sorbitet','symptoms':'Chest Burn','status':'Accepted'},
                     {'case_id':'HCCR0106','case_name':'Chronical Patient','patient_name':'Narendra Singh','doctor_name':'Debashis Panda','doctor_reg_no':'DD000006','disease':'Cardiac Arrest','medicine':'Sorbitet','symptoms':'Chest Burn','status':'Accepted'},
                     {'case_id':'HCCR0106','case_name':'Chronical Patient','patient_name':'Narendra Singh','doctor_name':'Debashis Panda','doctor_reg_no':'DD000006','disease':'Cardiac Arrest','medicine':'Sorbitet','symptoms':'Chest Burn','status':'Accepted'},
                    ]
        
        search_filter_list= {}
        if request.GET.get('case_id_num'):
            search_filter_list['case_id__icontains'] = request.GET.get('case_id_num')
        if request.GET.get('pat_name'):
            search_filter_list['patient_name__icontains'] = request.GET.get('pat_name')
        if request.GET.get('strt_date'):
            search_filter_list['start_date'] = request.GET.get('strt_date')
        if request.GET.get('end_date'):
            search_filter_list['end_date'] = request.GET.get('end_date')
        if request.GET.get('gender'):
            search_filter_list['gender'] = request.GET.get('gender')
        if request.GET.get('disease_name'):
            search_filter_list['disease__icontains'] = request.GET.get('disease_name')
        if request.GET.get('medi_name'):
            search_filter_list['medicine__icontains'] = request.GET.get('medi_name')
        if request.GET.get('symptoms_name'):
            search_filter_list['symptoms'] = request.GET.get('symptoms_name')
        if request.GET.get('location_name'):
            search_filter_list['location'] = request.GET.get('location_name')
        if request.GET.get('city_name'):
            search_filter_list['city'] = request.GET.get('city_name')
        if request.GET.get('state_name'):
            search_filter_list['state'] = request.GET.get('state_name')
            
        return render(request, 'case_history/dashboard.html',{'data_list':data_list,
                                                             'case_id':request.GET.get('case_id'),
                                                             'pat_name':request.GET.get('patient_name'),
                                                             'strt_date':request.GET.get('start_date'),
                                                             'end_date':request.GET.get('end_date'),
                                                             'disease_name':request.GET.get('disease'),
                                                             'medi_name':request.GET.get('medicine'),
                                                             'symptoms_name':request.GET.get('symptoms'),
#                                                            'symp_details_id':symp_details_id,
                                                             'selc_symptm':int(request.GET.get('symptoms')) if request.GET.get('symptoms') else None,
                                                             'symptoms_name':request.GET.get('symptoms'),
                                                             'location_name':request.GET.get('location'),
                                                             'city_name':request.GET.get('city'),
                                                             'state_name':request.GET.get('state'),
                                                              })
""" Dashboard functionality  - Ends"""