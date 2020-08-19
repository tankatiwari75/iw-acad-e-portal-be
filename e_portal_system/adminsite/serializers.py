from rest_framework import serializers
from .models import StudentRegistration


class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentRegistration
        fields = "__all__"

        def validate_name(self, first_name):
            if len(first_name) <= 2:
                raise serializers.ValidationError("Name should be greater than 2 letters");
            return first_name
