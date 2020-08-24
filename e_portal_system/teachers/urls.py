from django.urls import path
from teachers.views import AttendanceUploadsView, ResultUploadUploadView, GetSubjectsByTeacher, StudentListForAttendance

urlpatterns=[
    path('attendanceuploads/', AttendanceUploadsView.as_view()),
    path('resultuploads/', ResultUploadUploadView.as_view()),
    path("attendance/<int:class_number>/",StudentListForAttendance.as_view({'get':'list'})),
    path("<int:id>/<int:class_number>/",GetSubjectsByTeacher.as_view({'get':'list'})),

]

