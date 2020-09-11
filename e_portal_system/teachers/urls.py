from django.urls import path
from teachers.views import AttendanceUploadsView,StudentListForResult,Attendance,Result,GetSubjectsTeacher, ResultUploadUploadView, GetSubjectsByTeacher, StudentListForAttendance,FetchAttendanceByStudent,FetchResultByStudent
from rest_framework.routers import DefaultRouter

r= DefaultRouter()
r.register('update-attendance',Attendance,basename="attendance")
r.register('update-result',Result,basename="result")





urlpatterns=[
    path('attendanceuploads/', AttendanceUploadsView.as_view({'get':'list','post':'create'})),
    path('resultuploads/', ResultUploadUploadView.as_view({'get':'list','post':'create'})),
    path("<int:teacher_id>/<str:subject_name>/",StudentListForAttendance.as_view({'get':'list'})),
    path("result/<int:teacher_id>/<str:subject_name>/",StudentListForResult.as_view({'get':'list'})),
    
    path("getsubject/<int:teacher_id>/",GetSubjectsByTeacher.as_view({'get':'list'})),
    path("getsubjestteacher/<int:teacher_id>/<int:class_number>/",GetSubjectsTeacher.as_view({'get':'list'})),
    #for student
    path("attendance/<int:student_id>/",FetchAttendanceByStudent.as_view({'get':'list'})),
    path("result/<int:student_id>/",FetchResultByStudent.as_view({'get':'list'}))
]+r.urls

