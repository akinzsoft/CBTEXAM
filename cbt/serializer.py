from rest_framework import serializers
from .models import ScholarshipApplicant,Course,Question
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User


# class scholarshipapplicant(serializers.ModelSerializer):
#     class Meta:
#      model = scholarshipapplicant
#      fields = '__all__'
     
class courseserial(serializers.ModelSerializer):
    class Meta:
     model = Course
     fields = '__all__'
     
class questionserial(serializers.ModelSerializer):
    class Meta:
     model = Question
     fields = '__all__'
     
     
     
     
     
     
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2', 'first_name', 'last_name')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn’t match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            is_staff=True,
            
           
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    
class ScholarshipApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScholarshipApplicant
        fields = "__all__"
