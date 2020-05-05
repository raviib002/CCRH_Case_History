from django.urls import path, re_path
from user_profile import views as user_profile_views
from django.contrib.auth.views import PasswordResetConfirmView,PasswordResetCompleteView, PasswordResetView
from user_profile.forms import CustomSetPasswordForm, PasswordResetFormUnique, CustomPasswordChangeForm

app_name="user_profile"

urlpatterns = [
    path('check_user/', user_profile_views.check_user_api, name="check_user"),
    path('login/', user_profile_views.login_view, name="login"),
    path('logout/', user_profile_views.logout_view, name='logout'),
    path('change_password/', user_profile_views.change_password, name='change_password'),
    path('forget_password/', user_profile_views.password_forgot, name='forget_password'),
    path('password-forgot/', user_profile_views.password_forgot, name='password_forgot'),
    #On click of password reset link, displaying a form to submit passwords.
    path('password_reset_<uidb64>_<token>/',PasswordResetConfirmView.as_view(
                                            form_class=CustomSetPasswordForm,
                                            template_name='user_profile/password_reset_confirm.html',
                                            success_url='/user/reset/done/'),
                                            name='password_reset_confirm'),
    #After password resetting done redirecting to a page having login link.
    path('reset/done/', PasswordResetCompleteView.as_view(
                                                template_name='user_profile/password_reset_complete.html'
                                                ), name='password_reset_complete'),
    path('registration/', user_profile_views.registration_step, name='registration'),
    path('profile_info/', user_profile_views.registration_profile_info, name='profile_info'),
    path('documentation_upload/', user_profile_views.registration_document_upload, name='documentation_upload'),
    path('register_success/', user_profile_views.registration_successfuly, name='register_success'),
    path('get_city_name/',  user_profile_views.get_city_based_on_state, name='get_city_name'),
    path('uploaded_document_downloaded/<str:doc_id>/',  user_profile_views.uploaded_document_downloaded, name='uploaded_document_downloaded'),
    path('view_registration_details/<str:notify_id>/', user_profile_views.view_registration_details, name='view_registration_details'),
    path('activate/<uidb64>/<token>/',user_profile_views.activate, name='activate'),
    ]