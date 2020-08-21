from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .serializers import (
                                CreateClassSerializers,
                                CreateSubjectSerializers,
                                NoticeUploadSerializers,
                                StudentModelSerializer,
                          )
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet

from .models import AddSubject, NoticeUpload, StudentRegistration


# Create your views here.
class ClassCreateAPIView(CreateAPIView):
    serializer_class=CreateClassSerializers

class CreateSubjectAPIView(ModelViewSet):
    serializer_class=CreateSubjectSerializers
    queryset=AddSubject.objects.all()

class NoticeBoardUploadView(ModelViewSet):
    serializer_class=NoticeUploadSerializers
    queryset=NoticeUpload.objects.all()

class StudentRegisterModelViewSet(ModelViewSet):
    serializer_class = StudentModelSerializer
    queryset = StudentRegistration.objects.all()


