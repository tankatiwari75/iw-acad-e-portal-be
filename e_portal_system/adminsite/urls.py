from django.urls import path
from .views import ClassCreateAPIView, CreateSubjectAPIView, NoticeBoardUploadView,TeacherRegisterModelViewSet, StudentRegisterModelViewSet , RoleforTeacherModelView,DirectMessageModelView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


r= DefaultRouter()
r.register('studentregister', StudentRegisterModelViewSet,basename="studentregister")
r.register('subjectregister', CreateSubjectAPIView,basename="subjectregister")
r.register('noticeboard', NoticeBoardUploadView,basename="notice")
r.register('roleforteacher', RoleforTeacherModelView,basename="role")
r.register('directmessage', DirectMessageModelView,basename="message")
r.register('teacherregister',TeacherRegisterModelViewSet,basename="teacherregister")
# r.register("admindatas", AdminLoginAPIVeiw)

app_name="adminsite"
urlpatterns=[
    path('add-classnumber/',ClassCreateAPIView.as_view()),
    #path('admin-datas/', AdminLoginAPIVeiw.as_view()),
    path('login/', obtain_auth_token)
]+r.urls
