from django.urls import path
from .views import ClassCreateAPIView, CreateSubjectAPIView, NoticeBoardUploadView, StudentRegisterModelViewSet, RoleforTeacherModelView, DirectMessageModelView, TeacherRegistrationModelViewSet
from rest_framework.routers import DefaultRouter


r = DefaultRouter()
r.register('studentregister', StudentRegisterModelViewSet)
r.register('teacherregister', TeacherRegistrationModelViewSet)
r.register('subjectregister', CreateSubjectAPIView)
r.register('noticeboard', NoticeBoardUploadView)
r.register('roleforteacher', RoleforTeacherModelView)
r.register('directmessage', DirectMessageModelView)

app_name = "adminsite"
urlpatterns = [
    path('add-classnumber/',ClassCreateAPIView.as_view()),
]+r.urls
