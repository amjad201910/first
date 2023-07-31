from rest_framework import serializers
from .models import opinion, complaints








class opinionCreateSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = opinion
        fields = ['description']



class complaintsCreateSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = complaints
        fields = ['description']