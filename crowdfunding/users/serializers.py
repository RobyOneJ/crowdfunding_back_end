from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields ='__all__'
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


# Update User details function
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.first_name = validated_data.get('first name', instance.first_name)
        instance.last_name = validated_data.get('last name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
