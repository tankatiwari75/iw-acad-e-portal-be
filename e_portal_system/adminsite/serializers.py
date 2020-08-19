from adminsite.models import AddClassNumber, AddSubject, NoticeUpload

from rest_framework import serializers

class CreateClassSerializers(serializers.ModelSerializer):
    class Meta:
        model = AddClassNumber
        fields="__all__"

class CreateSubjectSerializers(serializers.ModelSerializer):
    class Meta:
        model=AddSubject
        fields="__all__"

class NoticeUploadSerializers(serializers.ModelSerializer):
    class Meta:
        model=NoticeUpload
        fields="__all__"
