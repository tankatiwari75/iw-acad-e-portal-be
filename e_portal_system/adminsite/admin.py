from django.contrib import admin

from adminsite.models import (AddSubject,
                              StudentRegistration,
                              AddClassNumber,
                              TeacherRegistration,
                              NoticeUpload,
                              RoleForTeacher,
                                DirectMessageModel
                              )

admin.site.register(AddClassNumber)

admin.site.register(AddSubject)
admin.site.register(StudentRegistration)
admin.site.register(TeacherRegistration)
admin.site.register(NoticeUpload)
admin.site.register(RoleForTeacher)
admin.site.register(DirectMessageModel)

