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
                                )

from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from .models import AddSubject, NoticeUpload, StudentRegistration , RoleForTeacher, DirectMessageModel, TeacherRegistration
from rest_framework.response import Response


# Create your views here.
class ClassCreateAPIView(CreateAPIView):
    serializer_class=CreateClassSerializers

class CreateSubjectAPIView(ModelViewSet):
    serializer_class = CreateSubjectSerializers
    queryset = AddSubject.objects.all()

class NoticeBoardUploadView(ModelViewSet):
    serializer_class = NoticeUploadSerializers
    queryset = NoticeUpload.objects.all()

class StudentRegisterModelViewSet(ModelViewSet):
    serializer_class = StudentModelSerializer
    queryset = StudentRegistration.objects.all()


class TeacherRegistrationModelViewSet(ModelViewSet):
    queryset = TeacherRegistration.objects.all()
    serializer_class = TeacherModelSerializer

class RoleforTeacherModelView(ModelViewSet):
    serializer_class = RoleForTeacherSerializer
    queryset = RoleForTeacher.objects.all()

# class DirectMessageModelView(ModelViewSet):
#     queryset = DirectMessageModel.objects.all()
#     serializer_class = DirectMessageSerializer



class DirectMessageModelView(ModelViewSet):
    def list(self, request, id):
        queryset = DirectMessageModel.objects.filter(id=id)
        serializer = DirectMessageSerializer(queryset, many=True)
        return Response(serializer.data)



