from django.shortcuts import render
# from rest_framework.generics import CreateAPIView
# from rest_framework.viewsets import ModelViewSet
# from .models import AddSubject, NoticeUpload, StudentRegistration

# Create your views here.
from django.shortcuts import render
from .serializers import (
                                CreateClassSerializers,
                                CreateSubjectSerializers,
                                NoticeUploadSerializers,
                                StudentModelSerializer,
                                RoleForTeacherSerializer,
                                DirectMessageSerializer,
                                TeacherModelSerializer,
                                TeacherRegistrationSerializers,
                                AdminLoginModelSerializer
                                )

from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import AddSubject, AddUser, NoticeUpload, StudentRegistration , RoleForTeacher ,DirectMessageModel, TeacherRegistration
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ClassCreateAPIView(CreateAPIView):
    serializer_class=CreateClassSerializers
    authentication_classes = [TokenAuthentication]

class AdminLoginAPIVeiw(ListAPIView):
    queryset = AddUser.objects.all()
    serializer_class =AdminLoginModelSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]



class CreateSubjectAPIView(ModelViewSet):

    serializer_class=CreateSubjectSerializers
    queryset=AddSubject.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class NoticeBoardUploadView(ModelViewSet):
    serializer_class=NoticeUploadSerializers
    queryset=NoticeUpload.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class StudentRegisterModelViewSet(ModelViewSet):
    serializer_class = StudentModelSerializer
    queryset = StudentRegistration.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class TeacherRegisterModelViewSet(ModelViewSet):
    serializer_class = TeacherRegistrationSerializers
    queryset = TeacherRegistration.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class TeacherRegistrationModelViewSet(ModelViewSet):
    queryset = TeacherRegistration.objects.all()
    serializer_class = TeacherModelSerializer

class RoleforTeacherModelView(ModelViewSet):
    serializer_class = RoleForTeacherSerializer
    queryset = RoleForTeacher.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

# class DirectMessageModelView(ModelViewSet):
#     queryset = DirectMessageModel.objects.all()
#     serializer_class = DirectMessageSerializer



class DirectMessageModelView(ModelViewSet):
    serializer_class = DirectMessageSerializer
    queryset = DirectMessageModel.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]



