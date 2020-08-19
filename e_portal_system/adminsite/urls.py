from django.urls import path
from .class_views import StudentRegister, StudentDetail
# app_name="adminsite"

urlpatterns =[
    path("studentregister/", StudentRegister.as_view()),


]
