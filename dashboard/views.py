from django.shortcuts import render
from core.models import User
from rest_framework import generics,viewsets,views
from .serializers import opinionSerializer, complaintsSerializer
from user.models import opinion,complaints
# from .permissions import adminonly



from rest_framework.response import Response
from core.models import User


from django.db.models import Count


class  country (views.APIView):


    def get(self, request, *args, **kwargs):
        
        return Response({ User.objects.values('country').filter(use=True).annotate(count=Count('country'))})

class opinionViewsets(viewsets.ModelViewSet):
    http_method_names=['get','delete','patch']

    serializer_class = opinionSerializer
    queryset=opinion.objects.all()

    
    # permission_classes = [ adminonly]
    


class complaintsViewsets(viewsets.ModelViewSet):
    http_method_names=['get','delete']

    serializer_class = complaintsSerializer
    queryset=complaints.objects.all()
    # permission_classes = [ adminonly]
    
