from django.db import models

from django.contrib.auth.models import AbstractUser


class AddUser(AbstractUser):
    middle_name = models.CharField(max_length=150, blank=True)


class AddClassNumber(models.Model):
    class_number = models.CharField(max_length=2,unique=True)

    def __str__(self):
        return self.class_number


class AddSubject(models.Model):
    class_number = models.ForeignKey(AddClassNumber, to_field="class_number", on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=30,unique=True)
    subject_syllabus = models.FileField(blank=True)

    def __str__(self):
        return self.subject_name


class StudentRegistration(models.Model):
    profile_picture = models.ImageField(null=True, blank=True)
    student_user = models.OneToOneField(AddUser,on_delete=models.CASCADE)
    admission_number = models.IntegerField(unique=True)
    class_number = models.ForeignKey(AddClassNumber, to_field="class_number", on_delete=models.CASCADE,null=True)
    age = models.IntegerField()
    GENDER_CHOICE = (
        ('M', 'Male'),
        ('F', "Female"),

    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)
    parents_number = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    address = models.TextField()

    def __str__(self):
        fullname = self.student_user.first_name + " " + self.student_user.last_name
        return fullname


class TeacherRegistration(models.Model):
    profile_picture = models.ImageField()
    
    teacher_user = models.OneToOneField(AddUser, on_delete=models.CASCADE)
    teacher_unique_id = models.IntegerField(unique=True)
    phone_no = models.CharField(max_length=10)
    qualifications = models.TextField()

    def __str__(self):
        fullname = self.teacher_user.first_name + " " + self.teacher_user.last_name
        return fullname


class NoticeUpload(models.Model):
    notice_title = models.CharField(max_length=200)
    notice_description = models.TextField()
    created_by = models.ForeignKey(AddUser,to_field="username", on_delete=models.CASCADE)
    time_changed = models.DateTimeField(auto_now=True)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.notice_title


class RoleForTeacher(models.Model):
    teacher_name = models.ForeignKey(TeacherRegistration, to_field="teacher_unique_id", on_delete=models.CASCADE)
    class_number = models.ForeignKey(AddClassNumber, to_field="class_number", on_delete=models.CASCADE)
    subject_name = models.ForeignKey(AddSubject,to_field="subject_name", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.teacher_name)


class DirectMessageModel(models.Model):
    teacher_name = models.ForeignKey(TeacherRegistration, to_field="teacher_unique_id", on_delete=models.CASCADE)
    student_admission_number = models.ForeignKey(StudentRegistration,to_field="admission_number", on_delete=models.CASCADE)
    message = models.TextField()
    attachment = models.ImageField(upload_to='media', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.teacher_name)


