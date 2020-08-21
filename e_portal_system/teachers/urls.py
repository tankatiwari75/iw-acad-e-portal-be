from django.urls import path
from .views import AttendanceUploadsView, ResultUploadUploadView

urlpatterns=[
    path('attendanceuploads/', AttendanceUploadsView.as_view()),
    path('resultuploads/', ResultUploadUploadView.as_view()),
]

