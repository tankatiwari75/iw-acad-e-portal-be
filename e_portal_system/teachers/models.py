from django.db import models
from adminsite.models import AddClassNumber, AddSubject, StudentRegistration, TeacherRegistration
from django.utils import timezone
# Create your models here.
# add two models here
# One for attendance upload
# One for Result Upload


class AttendanceUploads(models.Model):
    student_name = models.ForeignKey(StudentRegistration,related_name="student", on_delete=models.CASCADE)
    teacher_name = models.ForeignKey(TeacherRegistration, related_name="teacher", on_delete=models.CASCADE)
    subject_name = models.ForeignKey(AddSubject, related_name="subject", on_delete=models.CASCADE)
    student_id = models.ForeignKey(StudentRegistration, related_name="id22", on_delete=models.CASCADE)
    attendance =  models.BooleanField(default=False)
    date = models.DateField(default=timezone.now)


class ResultUpload(models.Model):
    student_name = models.ForeignKey(StudentRegistration,related_name="students", on_delete=models.CASCADE)
    teacher_name = models.ForeignKey(TeacherRegistration, related_name="teachers", on_delete=models.CASCADE)
    subject_name = models.ForeignKey(AddSubject, related_name="subjects", on_delete=models.CASCADE)
    student_id = models.ForeignKey(StudentRegistration, related_name="id11", on_delete=models.CASCADE)
    marks = models.IntegerField()
    
