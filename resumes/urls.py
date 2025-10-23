#resume_analysis/resumes/urls.py
from django.urls import path
from . import views

app_name = 'resumes'
urlpatterns = [
    path('', views.upload_resume, name='upload'),
    path('result/<int:pk>/', views.result_view, name='result'),
]
