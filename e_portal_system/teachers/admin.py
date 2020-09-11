from django.contrib import admin

# Register your models here.
from .models import AttendanceUploads, ResultUpload


admin.site.register(AttendanceUploads)
admin.site.register(ResultUpload)

