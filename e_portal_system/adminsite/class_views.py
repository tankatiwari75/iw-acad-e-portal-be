from rest_framework.response import Response
from rest_framework.views import APIView
from .models import StudentRegistration
from .serializers import StudentModelSerializer
from rest_framework import status


class StudentRegister(APIView):
    def get(self, request, *args, **kwargs):
        qs = StudentRegistration.objects.all()
        serializer = StudentModelSerializer(instance=qs, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def post(self, request, *args, **kwargs):
        serializer = StudentModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"message": "ok"}, status=status.HTTP_201_CREATED)


class StudentDetail(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"message":"this is detail page"})
