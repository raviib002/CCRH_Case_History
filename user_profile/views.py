import json
import random
import re
import string
import os
import datetime
from django.contrib.auth import views as auth_views
from django.db import connection
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from user_profile.forms import LoginForm, PasswordResetFormUnique
from django.http import HttpResponseRedirect, HttpResponse
from django.urls.base import reverse_lazy
from django.conf import settings
from user_profile.forms import ( CustomPasswordChangeForm,RegistrationStep3,RegistrationStep2,Uploadcertificates)
from django.contrib.auth import views as auth_views
from django.core.mail import (send_mail,
                              EmailMultiAlternatives,
                              EmailMessage
                              )
from django.utils.html import strip_tags, format_html
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
# from user_profile.models import UserProfile
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.utils.translation import ugettext as _
from utils.common_functions import (make_unique_username)
from notifications.signals import notify

from user_profile.models import (AdditionalProfile,PractCertificateUpload,
                                 PractDetails,EmailTemplate,Profilestatus,
                                 PractCsDetails,PractClinicalSettings)
from master.models import State,City,ClinicalSetting
from wsgiref.util import FileWrapper
import mimetypes
from django.utils.encoding import smart_str
from notifications.models import Notification
from notifications.views import mark_as_read
from django.http import JsonResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import (api_view,
                                       parser_classes,
                                       permission_classes,
                                       renderer_classes
                                       )
from rest_framework.authtoken.models import Token
from django.db.models.functions import Lower
from django.utils.encoding import force_bytes, force_text  
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from .tokens import account_activation_token  
from django.contrib.sites.models import Site
import base64


"""Case History Check User Existence Functionality - starts"""
@csrf_exempt
@parser_classes([JSONParser])
@api_view(['POST'])
def check_user_api(request):
    if request.method == "POST":
        data = request.data #Getting the parameters
        if data.get('username') and data.get('password'):
            user = authenticate(username=data.get('username'),
                                password=data.get('password')
                                )
        if user is not None:
            if user.is_active:
                results = {'status':1,
                           'message':user.id,
                         }
            else:
                message = _('Account is Blocked ! Please contact Admin')
                results = {'status':0,
                           'message':message,
                         }
            return Response(results)
"""Case History Check User Existence Functionality - ends"""

"""Case History Login Functionality - starts"""
@csrf_exempt
def login_view(request):
    ccrh_login = settings.CCRH_LOGIN_URL
    if request.method == 'GET':
        return HttpResponseRedirect(ccrh_login)
    if request.method == 'POST':
        username =request.POST['username']
        password =request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if user.is_superuser:
                    return HttpResponseRedirect('/admin/')
                else:
                    return HttpResponseRedirect(reverse_lazy('case_history:dashboard'))
        return HttpResponseRedirect(ccrh_login)
"""Case History Login Functionality - ends""" 
"""CCRH Logout Functionality - starts"""     
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGOUT_REDIRECT_URL)
"""CCRH Logout Functionality - ends"""
   
   
"""Forgot Password functionality. - Starts"""
def password_forgot(request):
    fp_form = PasswordResetFormUnique()
    success = request.session.pop('success_msg', None)
    #To show invalid email error message - starts
    old_post = request.session.pop('_old_post', None)
    if old_post:
        fp_form = PasswordResetFormUnique(old_post)
    
    if request.method == 'GET':
        form = PasswordResetFormUnique()
        return render(request, 'user_profile/forget_password.html',{'form':form,
                                                                    'fpform':fp_form,
                                                                    'old_post':old_post,
                                                                    'success_msg':success,
                                                                    })
    
    elif request.method == 'POST':
        form = PasswordResetFormUnique(request.POST)
        if form.is_valid():
            request.session['success_msg'] = _('We have sent a link to change your password. Kindly check your Email.')
            return auth_views.PasswordResetView.as_view(
                            form_class = PasswordResetFormUnique,
                            template_name = 'user_profile/forget_password.html',
                            email_template_name = 'user_profile/password_reset_email.html',
                            success_url = reverse_lazy('user_profile:forget_password'),
                            )(request)
        else:
            request.session['_old_post'] = request.POST
            return HttpResponseRedirect(reverse_lazy('user_profile:forget_password'))
            return render (request, 'user_profile/forget_password.html',{'form':form,
                                                                         'fpform':fp_form,
                                                                         })
    else:
        return HttpResponseRedirect(reverse_lazy('user_profile:forget_password'))
"""Forgot Password functionality. - Ends"""


"""Change Password functionality. - Starts"""
@login_required  
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            success= _('Password has been changed successfully.')
            return render(request, 'user_profile/password_change.html', {'form': form,
                                                                         'note':success})
        else:
            return render(request, 'user_profile/password_change.html', {'form': form })
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'user_profile/password_change.html', {'form': form })

"""Change Password functionality. - Ends"""

"""Registration profile step 1 starts here"""
def registration_step(request):
    if request.method == "GET":
        group_name=Group.objects.all()
        highlate_group_id = request.session.get('group_id', None)
        return render(request, 'user_profile/registration_step.html',{'group_name':group_name,
                                                                      'highlate_group_id':highlate_group_id})
    
    elif request.method == "POST":
        group_id = request.POST.get('added_role')
        request.session['group_id'] = group_id
        return HttpResponseRedirect(reverse_lazy('user_profile:profile_info'))
     
"""Registration Step2 Function Starts here"""
def registration_profile_info(request):
    if request.method == "GET":
        state_obj = city_name = additional_details = user_details = None
        state=State.objects.filter(status__status_name='Active')
        city_name=City.objects.filter(status__status_name='Active')
        #getting Group id based on the session 
        group_id = request.session.get('group_id', None)
        user_id_exist = request.session.get('user_id', None)
        if user_id_exist:
            try:
                additional_details = AdditionalProfile.objects.get(user=user_id_exist)
            except:
                additional_details =  None
        return render(request, 'user_profile/registration_profile_info.html',{'group_id':group_id,
                                                                              'state':state,
                                                                              'city_name':city_name,
                                                                              'additional_details':additional_details,
                                                                             })

    elif request.method == "POST":
             #Generating random password here
            random_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(8)])
             #Adding Data in user table
            if  request.POST.get('user_id'):
                user_id = User.objects.filter(id=request.POST.get('user_id')).update(first_name=request.POST.get('first_name'),
                                              last_name = request.POST.get('last_name'),
                                              email = request.POST.get('email'),
                                              )
                #updating group table
                user_group= User.groups.through.objects.get(user=request.POST.get('user_id'))
                user_group.group_id = request.POST.get('group_id')
                user_group.save()
                #creating Additional Profile starts here
                additiona_prf = AdditionalProfile.objects.filter(user=request.POST.get('user_id')).update(
                                                 state_id=request.POST.get('state_name') if request.POST.get('state_name') else None,
                                                 city_id=request.POST.get('city_name') if request.POST.get('city_name') else None,
                                                 mobile_no = request.POST.get('mobile_no') if request.POST.get('mobile_no') else None,
                                                 address_line1 = request.POST.get('address_line1') if request.POST.get('address_line1') else None,
                                                 address_line2 = request.POST.get('address_line2') if request.POST.get('address_line2') else None,
                                                 pincode = request.POST.get('pincode') if request.POST.get('pincode') else None,
                                                 )
                #sending Email After saving starts
                request.session['user_id'] = request.POST.get('user_id')
                return HttpResponseRedirect(reverse_lazy('user_profile:documentation_upload'))
            
            elif not User.objects.filter(email=request.POST.get('email')) and not  AdditionalProfile.objects.filter(mobile_no=request.POST.get('mobile_number')) .exists():
                user_id = User.objects.create_user(first_name=request.POST.get('first_name'),
                                              last_name = request.POST.get('last_name'),
                                              email = request.POST.get('email'),
                                              username = make_unique_username(request.POST.get('email')),
                                              is_active = 0,
                                              password =random_string)
                user_id.groups.add(request.POST.get('group_id'))
                #creating Additional Profile starts here
                additiona_prf = AdditionalProfile.objects.create(user=user_id,
                                                 state_id=request.POST.get('state_name') if request.POST.get('state_name') else None,
                                                 city_id=request.POST.get('city_name') if request.POST.get('city_name') else None,
                                                 mobile_no = request.POST.get('mobile_no') if request.POST.get('mobile_no') else None,
                                                address_line1 = request.POST.get('address_line1') if request.POST.get('address_line1') else None,
                                                address_line2 = request.POST.get('address_line2') if request.POST.get('address_line2') else None,
                                                pincode = request.POST.get('pincode') if request.POST.get('pincode') else None,
                                                 )
                #sending Email After saving starts
                request.session['user_id'] = additiona_prf.user_id  
                return HttpResponseRedirect(reverse_lazy('user_profile:documentation_upload'))
            else:
                already_exists=_('Mobile Number or Email already Exists')
                state=State.objects.filter(status__status_name="Active")
                city_name=City.objects.filter(state_id=request.POST.get('state_name'))
                return render(request, "user_profile/registration_profile_info.html",{'first_name':request.POST.get('first_name'),
                                                                                      'state':state,
                                                                                      'city_name':city_name,
                                                                                      'group_id':request.POST.get('group_id'),
                                                                                      'middle_name':request.POST.get('middle_name'),
                                                                                      'last_name':request.POST.get('last_name'),
                                                                                      'email':request.POST.get('email'),
                                                                                      'mobile_no' : request.POST.get('mobile_no'),
                                                                                     'address_line1':request.POST.get('address_line1'),
                                                                                     'address_line2': request.POST.get('address_line2') ,
                                                                                     'pincode' : request.POST.get('pincode'),
                                                                                      'state_id':int(request.POST.get('state_name')) if request.POST.get('state_name') else None,
                                                                                      'city_id':int(request.POST.get('city_name')) if request.POST.get('city_name') else None,
                                                                                      'message':already_exists,
                                                                      })
                
            
"""Registration Step3 Function Starts here"""
def registration_document_upload(request):
    if request.method == "GET":
        form = RegistrationStep3()
        state=State.objects.filter(status__status_name="Active")
        clinical_setting = ClinicalSetting.objects.filter(status__status_name="Active")
        return render(request, 'user_profile/registration_document_upload.html',{'form':form,
                                                                                 'clinical_setting':clinical_setting,
                                                                                 'state':state,
                                                                                 })
    elif request.method == "POST":
        form = RegistrationStep3(request.POST)
        if form.is_valid():
            data = {k: v for k, v in form.cleaned_data.items()}
            uploded_dcoument = request.FILES.get('data',None)
            #saving the practical details 
            practical_details = PractDetails.objects.create(user_id = request.session.get('user_id', None),
                                                                state_id = request.POST.get('state_name') if request.POST.get('state_name') else None,
                                                                cs_num = request.POST.get('clinical_settings'),
                                                                **data)
            #saving the uploaded certificate
            certicficate_upload=PractCertificateUpload.objects.create(pract_id = practical_details.id,
                                                      document_name = ("Registration Certificates"),
                                                      )
            if uploded_dcoument:
                certicficate_upload.document_path = uploded_dcoument
                certicficate_upload.save()
            #saving the multi clinical name and clinical address
            postdata_keys = [key.split('_')[1] for key in request.POST.keys() if re.match(r'^clinicalname_\d+', key)]
            if postdata_keys:
                for each in postdata_keys:
                    if request.POST.get("clinicalname_%s" % each, None):
                        clinical_name = request.POST.get("clinicalname_%s" % each, None)
                    else:
                        clinical_name = None
                    if request.POST.get("clinicaladress_%s" % each, None):
                        clinical_address = request.POST.get("clinicaladress_%s" % each, None)
                    else:
                        clinical_address = None
                    
                    if clinical_name and clinical_address:
                        PractCsDetails.objects.create(pract_id=practical_details.id,
                                                                         clinic_name=clinical_name,
                                                                         clinic_address=clinical_address,
                                                                         )
            #fetching the type of clinical name from the multiselected check box
            type_clinical = [key.split('_')[1] for key in request.POST.keys() if re.match(r'^typeclinical_\d+', key)]
            if type_clinical:
                for each in type_clinical:
                        PractClinicalSettings.objects.create(pract_id=practical_details.id, 
                                                                             cs_id=each,
                                                                             )
            
            #Sending an email verification to the user starts here
            if settings.SEND_MAIL_ALL_PLACE :
                current_site = get_current_site(request)  
                mail_subject = 'Activate your account.'  
                message = render_to_string('user_profile/acc_active_email.html', {  
                    'user': practical_details.user,  
                    'domain': current_site.domain,  
                    'uid': urlsafe_base64_encode(force_bytes(practical_details.user.id)).encode().decode(),  
                    'token': account_activation_token.make_token(practical_details.user),  
                    'scheme' : 'https' if request.is_secure() else 'http'
                })  
                to_email = practical_details.user.email
                email = EmailMessage(  
                    mail_subject, message, to=[to_email]  
                )  
                email.send()  
            content = "Registration Approval"
            if settings.SEND_NOTIFICATIONS_ALL_PLACE:
                notify.send(practical_details.user,
                            recipient=User.objects.filter(email=settings.ADMIN_REGISTRATION_EMAIL),
                            verb='New Registration Form',
                            description=content,
                            level='Newly Registered')
            request.session.pop('user_id', None)
            request.session.pop('group_id', None)
            return HttpResponseRedirect(reverse_lazy('user_profile:register_success'))
            
"""Registration Success page redirect view function starts here"""  
def registration_successfuly(request):
    if request.method == "GET":
        return render(request, 'user_profile/registration_success_page.html',{})
    
"""Activation Account based on the email verification starts here"""
def activate(request, uidb64, token):  
        try:  
            uid = force_text(urlsafe_base64_decode(uidb64))  
            user = User.objects.get(id=uid)  
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
            user = None  
        if user is not None and account_activation_token.check_token(user, token):  
            user.is_active = True  
            user.save()  
            return HttpResponse('Thank you for your email confirmation. Please wait for admin approval to start using CCRH portal.')
        else:
            return HttpResponse('You have already used this link for email verification. Please wait for admin approval to start using CCRH portal.')
    
"""Calling Ajax Based on the state showing City starts here"""
def get_city_based_on_state(request):
    if request.method == "GET":
        results=[]
        try:
            state_obj = State.objects.get(id = request.GET.get('state_name'))
        except:
            state_obj = None
        city_names = City.objects.filter(state_id = state_obj)
        for fos in city_names:
                         user_json = {}
                         user_json['id'] = fos.id
                         user_json['city_name'] = fos.city_name
                         results.append(user_json)
        return JsonResponse({'list':results
                                 }) 
    


"""Register uploaded certficate downloaded function starts here"""
def uploaded_document_downloaded(request,doc_id=None):
    if request.method == "GET":
        try:
            file_name = PractCertificateUpload.objects.get(id=doc_id).document_path
        except:
            file_name = None
        if file_name:
            file_path = settings.MEDIA_ROOT +'/'+ str(file_name)
            file_wrapper = FileWrapper(open(file_path,'rb'))
            file_mimetype = mimetypes.guess_type(file_path)
            response = HttpResponse(file_wrapper, content_type=file_mimetype )
            response['X-Sendfile'] = file_path
            response['Content-Length'] = os.stat(file_path).st_size
            response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(os.path.basename(file_name.file.name))
            return response
   
"""Subscriber photo download function Ends here"""


"""For getting the description of notifications - Starts"""
def view_registration_details(request, notify_id=None):
    if request.method == "GET":
        try:
            record = Notification.objects.get(id=notify_id, recipient_id=request.user)
        except:
            record = None
        try:
            certificate_upload = PractCertificateUpload.objects.get(pract__user_id = record.actor_object_id)
        except:
            certificate_upload = None
        try:
            aditional_profile = AdditionalProfile.objects.get(user_id = record.actor_object_id)
        except:
            aditional_profile = None
        profile_status = Profilestatus.objects.all()
        if record:
            #Marking as Read once the user viewed
            mark_as_read(request, slug=record.slug)
        succes_page = request.session.pop('succes_page', None)
        return render(request, "user_profile/view_registration_details.html", {'record':record,
                                                                        'profile_status':profile_status,
                                                                        'certificate_upload':certificate_upload,
                                                                        'aditional_profile':aditional_profile,
                                                                        'notify_id':notify_id,
                                                                        'succes_page':succes_page,
                                                                        })  
        
    elif request.method == "POST":
        #Generating random password here
        random_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(8)])
        
        #updating the profile information
        pract_obj = PractDetails.objects.filter(id = request.POST.get('practical_details_id')).update(pract_reg_no = request.POST.get('regsr_no'))
        try:
           user_obj = AdditionalProfile.objects.get(id = request.POST.get('additona_profile_id'))
           user_obj.profile_status_id = request.POST.get('prfile_status_id')
           if user_obj.profile_status.profile_status.lower() == "approved":
               user_obj.profile_approved_by_id = request.user
               user_obj.profile_approved_datetime = datetime.datetime.now().date()
               user_obj.save()
        except:
            user_obj = None
        try:
            password_update = User.objects.get(id = user_obj.user_id)
            password_update.set_password(random_string)
            password_update.save()
        except:
            password_update = None
        if settings.SEND_MAIL_ALL_PLACE and user_obj.profile_status.profile_status.lower() == "approved" :
            send_email = EmailTemplate.objects.get(email_code='CCEM001')
            subject = send_email.email_subject
            to_email = user_obj.user.email
            from_email, to = settings.ADMIN_EMAIL, [to_email]
            html_content = send_email.email_body.format(user_name=user_obj.user.first_name + user_obj.user.last_name,
                                                        email_id = user_obj.user.email,
                                                            password=random_string)
            text_content = format_html(html_content)
            email = EmailMultiAlternatives(subject,
                                            text_content, 
                                            from_email, 
                                            to)
            email.content_subtype = 'html'
            email.send()
            
        if settings.SEND_MAIL_ALL_PLACE and request.POST.get('message'):
            send_email = EmailTemplate.objects.get(email_code='CCEM002')
            subject = send_email.email_subject
            to_email = user_obj.user.email
            from_email, to = settings.ADMIN_EMAIL, [to_email]
            html_content = send_email.email_body.format(user_name=user_obj.user.first_name + user_obj.user.last_name,
                                                        message = request.POST.get('message'),
                                                            )
            text_content = format_html(html_content)
            email = EmailMultiAlternatives(subject,
                                            text_content, 
                                            from_email, 
                                            to)
            email.content_subtype = 'html'
            email.send()
#             #sending Email After saving ends
        request.session['succes_page'] = "Registration Profile Has Been Updated Successfully"
        return HttpResponseRedirect(reverse_lazy('user_profile:view_registration_details',args=[str(request.POST.get('notify_id'))]))
"""For getting the description of notifications - Ends""" 