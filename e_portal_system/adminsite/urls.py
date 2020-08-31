from django.urls import path
from .views import ClassCreateAPIView, AdminLoginAPIVeiw, CreateSubjectAPIView, NoticeBoardUploadView,TeacherRegisterModelViewSet, StudentRegisterModelViewSet , RoleforTeacherModelView,DirectMessageModelView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


r= DefaultRouter()
r.register('studentregister', StudentRegisterModelViewSet)
r.register('subjectregister', CreateSubjectAPIView)
r.register('noticeboard', NoticeBoardUploadView)
r.register('roleforteacher', RoleforTeacherModelView)
r.register('directmessage', DirectMessageModelView)
r.register('teacherregister',TeacherRegisterModelViewSet)
# r.register("admindatas", AdminLoginAPIVeiw)

app_name="adminsite"
urlpatterns=[
    path('add-classnumber/',ClassCreateAPIView.as_view()),
    path('admin-datas/', AdminLoginAPIVeiw.as_view()),
    path('login/', obtain_auth_token)
]+r.urls
