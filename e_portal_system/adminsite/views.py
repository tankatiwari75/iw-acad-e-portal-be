from django.shortcuts import render
# from rest_framework.generics import CreateAPIView
# from rest_framework.viewsets import ModelViewSet
# from .models import AddSubject, NoticeUpload, StudentRegistration
from rest_framework.response import Response

# Create your views here.
from django.shortcuts import render
from .serializers import (
    CreateClassSerializers,
    CreateSubjectSerializers,
    NoticeUploadSerializers,
    StudentModelSerializer,
    RoleForTeacherSerializer,
    DirectMessageSerializer,
    TeacherRegistrationSerializers,
    AdminLoginModelSerializer
)

from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.viewsets import ModelViewSet
from .models import (
    AddSubject,
    AddUser,
    NoticeUpload,
    StudentRegistration,
    RoleForTeacher,
    DirectMessageModel,
    TeacherRegistration,
    AddClassNumber

)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated



class StudentRegisterModelViewSet(ModelViewSet):
    serializer_class= StudentModelSerializer

    def get_queryset(self):
        students= StudentRegistration.objects.all()
        return students

    def create(self,request,*args,**kwargs):
        post_data = request.data

        password=post_data["student_user"]["password"]
        new_user = AddUser.objects.create(
            first_name=post_data["student_user"]["first_name"],
            last_name=post_data["student_user"]["last_name"],
            username=post_data["student_user"]["username"],
            email=post_data["student_user"]["email"],

        )

        new_user.set_password(raw_password=password)
        new_user.save()


        new_student_user= StudentRegistration.objects.create(
                student_user= new_user,
                profile_picture=post_data["profile_picture"],
                admission_number= post_data["admission_number"],
    
                age=post_data["age"],
                gender=post_data["gender"],
                parents_number=post_data["parents_number"],
                date_of_birth=post_data["date_of_birth"],
                address=post_data["address"]
        )
        new_student_user.save()

        serializer= StudentModelSerializer(new_student_user)
        return Response(serializer.data)

# Create your views here.
class ClassCreateAPIView(CreateAPIView):
    serializer_class = CreateClassSerializers
    queryset = AddClassNumber.objects.all()
    authentication_classes = [TokenAuthentication]


# class AdminLoginAPIVeiw(ListAPIView):
#     queryset = AddUser.objects.all()
#     serializer_class = AdminLoginModelSerializer
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]


class CreateSubjectAPIView(ModelViewSet):
    serializer_class = CreateSubjectSerializers
    queryset = AddSubject.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class NoticeBoardUploadView(ModelViewSet):
    serializer_class = NoticeUploadSerializers
    queryset = NoticeUpload.objects.all()
    

#
# class StudentRegisterModelViewSet(ModelViewSet):
#     serializer_class = StudentModelSerializer
#     queryset = StudentRegistration.objects.all()
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]


class TeacherRegisterModelViewSet(ModelViewSet):
    serializer_class = TeacherRegistrationSerializers

    def get_queryset(self):
        students = TeacherRegistration.objects.all()
        return students

    def create(self, request, *args, **kwargs):
        post_data = request.data


        new_user = AddUser.objects.create(
            first_name=post_data["teacher_user"]["first_name"],
            last_name=post_data["teacher_user"]["last_name"],
            username=post_data["teacher_user"]["username"],
            email=post_data["teacher_user"]["email"],
        )

        new_user.set_password(raw_password=post_data["teacher_user"]["password"])
        new_user.save()

        new_teacher_user = TeacherRegistration.objects.create(
            teacher_user=new_user,
            profile_picture=post_data["profile_picture"],
            teacher_unique_id=post_data["teacher_unique_id"],
            phone_no=post_data["phone_no"],
            qualifications=post_data["qualifications"]
        )

        new_teacher_user.save()

        serializer = TeacherRegistrationSerializers(new_teacher_user)
        return Response(serializer.data)


class RoleforTeacherModelView(ModelViewSet):
    serializer_class = RoleForTeacherSerializer
    queryset = RoleForTeacher.objects.all()
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class DirectMessageModelView(ModelViewSet):
    serializer_class = DirectMessageSerializer
    queryset = DirectMessageModel.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
