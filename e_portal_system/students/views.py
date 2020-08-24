from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from .serializers import SyllabusViewModelSerializer
#from adminsite.serializers import GetStudentSerializers, FetchSubject, CreateSubjectSerializers
from adminsite.models import AddSubject


class SyllabusView(viewsets.ViewSet):

    def list(self, request, class_number):
        queryset = AddSubject.objects.filter(class_number = class_number)
        serializer = SyllabusViewModelSerializer(queryset, many = True) 
        #serializer = CreateSubjectSerializers(queryset, many = True) 
        return Response(serializer.data) 



