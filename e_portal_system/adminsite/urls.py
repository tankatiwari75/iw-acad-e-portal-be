from django.urls import path
from .viewset_views import StudentRegisterModelViewSet
from rest_framework.routers import DefaultRouter

r= DefaultRouter()
r.register('studentregister', StudentRegisterModelViewSet)


# app_name="adminsite"

urlpatterns =[

] + r.urls
