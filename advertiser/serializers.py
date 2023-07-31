from rest_framework import serializers
from core.models import User
from .models import advertisement








class advertiserCreateSerializer(serializers.ModelSerializer):
   
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ['phone','password']

    def create(self, validated_data):

       
            validated_data['group']='advertiser'
            
            data=super().create(validated_data)
            
            return data
        

class advertisementSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = advertisement
        fields = ['pk','name','country','description','URL','image','cative']
        extra_kwargs = {'cative': {'read_only': True}}
    
    def create(self, validated_data):
        data=advertisement.objects.create(user=self.context['request'].user,**validated_data)

        
        return data
    
    
