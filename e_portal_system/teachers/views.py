from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .serializers import (
                                AttendanceUploadsModelSerializer,
                                ResultUploadModelSerializer,
                          )
from rest_framework.generics import CreateAPIView
from .models import AttendanceUploads, ResultUpload


# Create your views here.
class AttendanceUploadsView(CreateAPIView):
    serializer_class = AttendanceUploadsModelSerializer
    queryset = AttendanceUploads.objects.all()


class ResultUploadUploadView(CreateAPIView):
    serializer_class = ResultUploadModelSerializer
    queryset = ResultUpload.objects.all()


