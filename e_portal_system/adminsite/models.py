from django.db import models

from django.contrib.auth.models import AbstractUser


class AddUser(AbstractUser):
    middle_name = models.CharField(max_length=150, blank=True)


class AddClassNumber(models.Model):
    class_number = models.CharField(max_length=2)

    def __str__(self):
        return self.class_number


class AddSubject(models.Model):
    class_number = models.ForeignKey(AddClassNumber, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=30)
    subject_syllabus = models.FileField(blank=True)

    def __str__(self):
        return self.subject_name


class StudentRegistration(models.Model):
    profile_picture = models.ImageField(null=True, blank=True   )

    first_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()
    admission_number = models.IntegerField(unique=True)
    class_number = models.ForeignKey(AddClassNumber, on_delete=models.CASCADE)
    age = models.IntegerField()
    GENDER_CHOICE = (
        ('M', 'Male'),
        ('F', "Female"),

    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)
    parents_number = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    address = models.TextField()
    password = models.CharField(max_length=150)

    def __str__(self):
        fullname = self.first_name + " " + self.last_name
        return fullname


class TeacherRegistration(models.Model):
    profile_picture = models.ImageField()
    first_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone_no = models.CharField(max_length=10)
    qualifications = models.TextField()
    password = models.CharField(max_length=50)

    def __str__(self):
        fullname = self.first_name + " " + self.last_name
        return fullname


class NoticeUpload(models.Model):
    notice_title = models.CharField(max_length=200)
    notice_description = models.TextField()
    time_changed = models.DateTimeField(auto_now=True)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.notice_title


class RoleForTeacher(models.Model):
    teacher_name = models.ForeignKey(TeacherRegistration, on_delete=models.CASCADE)
    class_number = models.ForeignKey(AddClassNumber, on_delete=models.CASCADE)
    subject_name = models.ForeignKey(AddSubject, on_delete=models.CASCADE)
    # description = models.TextField(blank=False, null=True)

    def __str__(self):
        return str(self.teacher_name)


class DirectMessageModel(models.Model):
    teacher_name = models.ForeignKey(TeacherRegistration, on_delete=models.CASCADE)
    student_name = models.ForeignKey(StudentRegistration,on_delete=models.CASCADE)
    message = models.TextField(blank=True, null=False)
    attachment = models.FileField(upload_to='media', null=True, blank=True)
    # attachment = models.ImageField(upload_to='media',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.teacher_name

