from django.shortcuts import render
from core.models import User
from rest_framework import generics,viewsets,views
from .serializers import advertiserCreateSerializer, advertisementSerializer
from .models import advertisement
from .permissions import advertiseronly
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password


class advertiserCreat(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = advertiserCreateSerializer
    def post(self, request, *args, **kwargs):
        data = request.data

         
        hashed_password = make_password(data['password'])
        if User.objects.filter(phone=data['phone']).update(group='advertiser',password=hashed_password):

            
           
            return Response({"phone":data['phone']}, status=status.HTTP_201_CREATED)
  
        else:
        
            return self.create(request, *args, **kwargs)




class advertisementViewsets(viewsets.ModelViewSet):
    serializer_class = advertisementSerializer
    permission_classes = [ advertiseronly]
    
    def get_queryset(self):
        self.queryset = advertisement.objects.filter(user=self.request.user)
        return super().get_queryset()


