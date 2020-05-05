from django.urls import path, re_path
from case_history import views as case_history_views

app_name="case_history"

urlpatterns = [
    path('dashboard/', case_history_views.dashboard, name='dashboard'),
    ]
