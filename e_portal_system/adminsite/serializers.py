from .models import AddClassNumber, AddSubject, AddUser, NoticeUpload, StudentRegistration, RoleForTeacher, DirectMessageModel, TeacherRegistration
from rest_framework import serializers

class AdminLoginModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AddUser
        fields = ["id","username","first_name","last_name","email","password"]
        depth=1


class StudentModelSerializer(serializers.ModelSerializer):
    student_user=AdminLoginModelSerializer(required=True)

    class Meta:
        model = StudentRegistration
        fields = "__all__"



class GetStudentSerializers(serializers.ModelSerializer):
    
    class Meta:
        model= StudentRegistration
        fields=["student_user","id","admission_number","class_number"]


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
        fields=["class_number","teacher_name","subject_name"]

class TeacherRegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model= TeacherRegistration
        fields="__all__"
