from django.db import models
from adminsite.models import AddClassNumber, AddSubject, StudentRegistration, TeacherRegistration
from django.utils import timezone


class AttendanceUploads(models.Model):
    student_id=models.ForeignKey(StudentRegistration,to_field="admission_number", on_delete=models.CASCADE)
    teacher_id= models.ForeignKey(TeacherRegistration, to_field="teacher_unique_id", on_delete=models.CASCADE,default=1)
    subject_name= models.ForeignKey(AddSubject, to_field="subject_name", on_delete=models.CASCADE)
    class_number = models.ForeignKey(AddClassNumber, to_field="class_number", on_delete=models.CASCADE,default=10)
    class_held= models.IntegerField(default=0)
    class_present = models.IntegerField(default=0)

class ResultUpload(models.Model):
    student_id=models.ForeignKey(StudentRegistration,to_field="admission_number", on_delete=models.CASCADE)
    teacher_name= models.ForeignKey(TeacherRegistration, to_field="teacher_unique_id", on_delete=models.CASCADE)
    subject_name= models.ForeignKey(AddSubject, to_field="subject_name", on_delete=models.CASCADE)
    class_number = models.ForeignKey(AddClassNumber, to_field="class_number", on_delete=models.CASCADE,default=1)
    marks=models.IntegerField()
    pass_status = models.BooleanField(default=False)