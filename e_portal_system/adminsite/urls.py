from django.urls import path
<<<<<<< HEAD
from adminsite.views import ClassCreateAPIView, CreateSubjectAPIView, NoticeBoardUploadView


from rest_framework.routers import DefaultRouter
r=DefaultRouter()

r.register('add-subject',CreateSubjectAPIView)
r.register('add-notice',NoticeBoardUploadView)

app_name="adminsite"
urlpatterns=[
    path('add-classnumber/',ClassCreateAPIView.as_view()),
]+r.urls
=======
from .viewset_views import StudentRegisterModelViewSet
from rest_framework.routers import DefaultRouter

r= DefaultRouter()
r.register('studentregister', StudentRegisterModelViewSet)


# app_name="adminsite"

urlpatterns =[

] + r.urls
>>>>>>> origin/dev
