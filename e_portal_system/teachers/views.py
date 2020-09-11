
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from adminsite.models import StudentRegistration, RoleForTeacher, AddSubject
from adminsite.serializers import GetStudentSerializers, FetchSubject,CreateSubjectSerializers
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from teachers.serializers import (
                                AttendanceUploadsModelSerializer,
                                ResultUploadModelSerializer,
                          )
from rest_framework.generics import CreateAPIView
from teachers.models import AttendanceUploads, ResultUpload
from django.forms import forms


class Attendance(ModelViewSet):
    serializer_class = AttendanceUploadsModelSerializer
    queryset = AttendanceUploads.objects.all()

class Result(ModelViewSet):
    serializer_class = ResultUploadModelSerializer
    queryset = ResultUpload.objects.all()

# Create your views here.
class AttendanceUploadsView(ModelViewSet):
    serializer_class = AttendanceUploadsModelSerializer
    queryset = AttendanceUploads.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        subject_name=serializer.validated_data['subject_name']
        student_id= serializer.validated_data["student_id"]
        class_number= serializer.validated_data["class_number"]
        teacher_id= serializer.validated_data["teacher_id"]
        class_present= serializer.validated_data["class_present"]
        class_held=serializer.validated_data["class_held"]
        if AttendanceUploads.objects.filter(student_id=student_id,subject_name=subject_name).exists():
            raise forms.ValidationError("This student already added")
        else:
            AttendanceUploads.objects.create(
                student_id=student_id,
                teacher_id=teacher_id,
                subject_name=subject_name,
                class_number= class_number,
                class_present= class_present,
                class_held= class_held)   
        return Response(serializer.data)

class ResultUploadUploadView(ModelViewSet):
    serializer_class = ResultUploadModelSerializer
    queryset = ResultUpload.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        subject_name=serializer.validated_data['subject_name']
        student_id= serializer.validated_data["student_id"]
        if ResultUpload.objects.filter(subject_name=subject_name).exists():
            if ResultUpload.objects.filter(student_id=student_id).exists():
                raise forms.ValidationError("This student already added")
            else:
                self.perform_create(serializer)        
        return Response(serializer.data)

class StudentListForResult(viewsets.ViewSet):

    def list(self, request, teacher_id, subject_name):
        queryset = ResultUpload.objects.filter(teacher_name=teacher_id,subject_name=subject_name)
        serializer = ResultUploadModelSerializer(queryset, many=True)
        return Response(serializer.data)

#to get the list of students classWises
class StudentListForAttendance(viewsets.ViewSet):

    def list(self, request, teacher_id, subject_name):
        queryset = AttendanceUploads.objects.filter(teacher_id=teacher_id,subject_name=subject_name)
        serializer = AttendanceUploadsModelSerializer(queryset, many=True)
        return Response(serializer.data)


# For teacher to get subjects based on class_number
class GetSubjectsByTeacher(viewsets.ViewSet):
    
    def list(self, request,teacher_id):
        queryset=RoleForTeacher.objects.filter(teacher_name=teacher_id)
        serializer = FetchSubject(queryset, many=True)
        return Response(serializer.data)

class GetSubjectsTeacher(viewsets.ViewSet):
    
    def list(self, request,teacher_id, class_number):
        queryset=RoleForTeacher.objects.filter(teacher_name=teacher_id, class_number=class_number)
        serializer = FetchSubject(queryset, many=True)
        return Response(serializer.data)



class FetchAttendanceByStudent(viewsets.ViewSet):

    def list(self, request,student_id):
        queryset = AttendanceUploads.objects.filter(student_id=student_id)
        serializer = AttendanceUploadsModelSerializer(queryset, many=True)
        return Response(serializer.data)

class FetchResultByStudent(viewsets.ViewSet):
    def list(self, request,student_id):
        queryset = ResultUpload.objects.filter(student_id=student_id)
        serializer = ResultUploadModelSerializer(queryset, many=True)
        return Response(serializer.data)