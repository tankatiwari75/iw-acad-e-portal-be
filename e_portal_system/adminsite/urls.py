from django.urls import path
from .viewset_views import StudentRegisterModelViewSet
from .views import ClassCreateAPIView, CreateSubjectAPIView, NoticeBoardUploadView
from rest_framework.routers import DefaultRouter


r= DefaultRouter()
r.register('studentregister', StudentRegisterModelViewSet)
r.register('subjectregister', CreateSubjectAPIView)
r.register('noticeboard', NoticeBoardUploadView)


app_name="adminsite"
urlpatterns=[
    path('add-classnumber/',ClassCreateAPIView.as_view()),
]+r.urls
