from django.urls import path
from teachers.views import AttendanceUploadsView, ResultUploadUploadView, GetSubjectsByTeacher, StudentListForAttendance,FetchAttendanceByStudent,FetchResultByStudent

urlpatterns=[
    path('attendanceuploads/', AttendanceUploadsView.as_view()),
    path('resultuploads/', ResultUploadUploadView.as_view()),
    path("<int:class_number>/<int:teacher_id>/<str:subject_name>/",StudentListForAttendance.as_view({'get':'list'})),
    path("<int:teacher_id>/",GetSubjectsByTeacher.as_view({'get':'list'})),
    path("attendance/<int:student_id>/",FetchAttendanceByStudent.as_view({'get':'list'})),
    path("result/<int:student_id>/",FetchResultByStudent.as_view({'get':'list'}))
]

