
from .models import opinion,complaints
from rest_framework import generics,viewsets,views
from .serializers import opinionCreateSerializer, complaintsCreateSerializer



class opinionCreate(generics.CreateAPIView):
    queryset = opinion.objects.all()
    serializer_class = opinionCreateSerializer




class complaintsCreate(generics.CreateAPIView):
    queryset = complaints.objects.all()
    serializer_class = complaintsCreateSerializer