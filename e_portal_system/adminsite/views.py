from django.shortcuts import render
from .serializers import (
                                CreateClassSerializers,
                                CreateSubjectSerializers,
                                NoticeUploadSerializers,
                                StudentModelSerializer,
                                RoleForTeacherSerializer,
                                DirectMessageSerializer,
                          )
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from .models import AddSubject, NoticeUpload, StudentRegistration, RoleForTeacher, DirectMessageModel


# Create your views here.
class ClassCreateAPIView(CreateAPIView):
    serializer_class = CreateClassSerializers

class CreateSubjectAPIView(ModelViewSet):
    serializer_class = CreateSubjectSerializers
    queryset = AddSubject.objects.all() 

class NoticeBoardUploadView(ModelViewSet):
    serializer_class = NoticeUploadSerializers
    queryset = NoticeUpload.objects.all()

class StudentRegisterModelViewSet(ModelViewSet):
    serializer_class = StudentModelSerializer
    queryset = StudentRegistration.objects.all() 

class RoleforTeacherModelView(ModelViewSet):
    serializer_class = RoleForTeacherSerializer
    queryset = RoleForTeacher.objects.all()

class DirectMessageModelView(ModelViewSet):
    serializer_class = DirectMessageSerializer
    queryset = DirectMessageModel.objects.all()     

class RoleforTeacherModelView(ModelViewSet):
    serializer_class = RoleForTeacherSerializer
    queryset = RoleForTeacher.objects.all()

class DirectMessageModelView(ModelViewSet):
    serializer_class = DirectMessageSerializer
    queryset = DirectMessageModel.objects.all()



