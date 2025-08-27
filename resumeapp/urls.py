from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('resumes/upload/', views.upload_resume, name='resume_upload'),
    path('resumes/', views.resume_list, name='resume_list'),
    path('resumes/<int:pk>/', views.resume_detail, name='resume_detail'),
]
