from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer




class TokenObtainPairSerializerNew(TokenObtainPairSerializer):
    def validate(self, attrs) :



         data= super().validate(attrs)
         data['phone'] = self.user.phone
         data['country'] = self.user.country




         return data
