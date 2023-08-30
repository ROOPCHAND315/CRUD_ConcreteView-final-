from .models import StudentModel
from .serializers import StudentSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

class LCStudent(ListCreateAPIView):
    queryset=StudentModel.objects.all()
    serializer_class=StudentSerializer

class RUDStudent(RetrieveUpdateDestroyAPIView):
    queryset=StudentModel.objects.all()
    serializer_class=StudentSerializer    