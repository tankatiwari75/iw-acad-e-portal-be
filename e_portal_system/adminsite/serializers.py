from .models import AddClassNumber, AddSubject, AddUser, NoticeUpload, StudentRegistration, RoleForTeacher, DirectMessageModel, TeacherRegistration
from rest_framework import serializers

class AdminLoginModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddUser
        fields = ["id","username","first_name","last_name","email"]


class StudentModelSerializer(serializers.ModelSerializer):
    student_user=AdminLoginModelSerializer(required=True)
    class Meta:
        model = StudentRegistration
        # fields = "__all__"
        fields = [
            "student_user",
            'admission_number',
            'class_number',
            'age',
            'gender',
            'parents_number',
            'date_of_birth',
            'address',
        ]
#
#         def create(self, validated_data):
#             user_data = validated_data.pop('student_user')
#             user = AdminLoginModelSerializer.create(AdminLoginModelSerializer(), validated_data=user_data)
#             student, created = StudentRegistration.objects.update_or_create(
#                 user=user,
#                 subject_major=validated_data.pop('')
#             )
#             return student

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
    student_user=AdminLoginModelSerializer(required=True)
    class Meta:
        model= StudentRegistration
        fields=["student_user","id","admission_number","class_number"]
        depth=1

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

class TeacherRegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model= TeacherRegistration
        fields="__all__"
