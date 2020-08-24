from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from adminsite.models import StudentRegistration, RoleForTeacher, AddSubject
from adminsite.serializers import GetStudentSerializers, FetchSubject, CreateSubjectSerializers
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from teachers.serializers import (
                                   AttendanceUploadsModelSerializer,
                                   ResultUploadModelSerializer,
                                 )
from rest_framework.generics import CreateAPIView
from teachers.models import AttendanceUploads, ResultUpload

class AttendanceUploadsView(CreateAPIView):
    serializer_class = AttendanceUploadsModelSerializer
    queryset = AttendanceUploads.objects.all() 


class ResultUploadUploadView(CreateAPIView):
    serializer_class = ResultUploadModelSerializer
    queryset = ResultUpload.objects.all()

#to get the list of students classWises
class StudentListForAttendance(viewsets.ViewSet): 

    def list(self, request, class_number):
        queryset = StudentRegistration.objects.filter(class_number=class_number)
        serializer = GetStudentSerializers(queryset, many=True)
        return Response(serializer.data)


# For teacher to get subjects based on class_number
class GetSubjectsByTeacher(viewsets.ViewSet):
    
    def list(self, request, id, class_number):
        queryset=RoleForTeacher.objects.filter(id=id, class_number=class_number)
        serializer = FetchSubject(queryset, many=True)
        return Response(serializer.data)    


