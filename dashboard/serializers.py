from rest_framework import serializers
from user.models import opinion, complaints








class opinionSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = opinion
        fields = ['pk','description','active']
        extra_kwargs = {'description': {'read_only': True}}




class complaintsSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = complaints
        fields = ['pk','description']