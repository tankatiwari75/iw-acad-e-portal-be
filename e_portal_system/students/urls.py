from django.urls import path
from .views import SyllabusView

urlpatterns=[

    path('syllabus/<int:class_number>/', SyllabusView.as_view(({'get': 'list'})))

]