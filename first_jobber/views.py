from rest_framework import generics
from .serializers import InsuranceSerializer, UserSerializer, CoverageSerializer
from .models import Insurance, User, Coverage

# Create your views here.

class InsuranceList(generics.ListCreateAPIView):
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer

class InsuranceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CoverageList(generics.ListCreateAPIView):
    queryset = Coverage.objects.all()
    serializer_class = CoverageSerializer

class CoverageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coverage.objects.all()
    serializer_class = CoverageSerializer