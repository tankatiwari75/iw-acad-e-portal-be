from rest_framework import serializers
from .models import AttendanceUploads, ResultUpload

class AttendanceUploadsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceUploads
        fields = "__all__"

class ResultUploadModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultUpload
        fields = "__all__"