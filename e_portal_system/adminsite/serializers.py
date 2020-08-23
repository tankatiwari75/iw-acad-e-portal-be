from .models import AddClassNumber, AddSubject, NoticeUpload, StudentRegistration, RoleForTeacher, DirectMessageModel
from rest_framework import serializers

class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentRegistration
        # fields = "__all__"
        fields = [
            'profile_picture',
            'first_name',
            'middle_name',
            'last_name',
            'email',
            'admission_number',
            'age',
            'gender',
            'parents_number',
            'date_of_birth',
            'address',
            'password',
            'class_number',
        ]

        # def validate_name(self, first_name):
        #     if len(first_name) <= 2:
        #         raise serializers.ValidationError("Name should be greater than 2 letters");
        #     return first_name
        #
        # def validate(self, data):
        #     name = data['first_name']
        #     if len(name)  <=2:
        #         raise serializers.ValidationError("Name should be greater than 2 letters")
        #     return data

class GetStudentSerializers(serializers.ModelSerializer):
    class Meta:
        model= StudentRegistration
        fields=["id","first_name","last_name"]

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

class RoleForTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleForTeacher
        fields="__all__"

class DirectMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectMessageModel
        fields = "__all__"
        
class FetchSubject(serializers.ModelSerializer):
    class Meta:
        model= RoleForTeacher
        fields=["subject_name"]