from rest_framework import serializers
from adminsite.models import AddSubject


class SyllabusViewModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddSubject 
        fields = [
            'class_number',
            'subject_name',
            'subject_syllabus',
        ]  

        