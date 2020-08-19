from rest_framework.viewsets import ModelViewSet
from .serializers import StudentModelSerializer
from .models import StudentRegistration


class StudentRegisterModelViewSet(ModelViewSet):
    serializer_class = StudentModelSerializer
    queryset = StudentRegistration.objects.all()



