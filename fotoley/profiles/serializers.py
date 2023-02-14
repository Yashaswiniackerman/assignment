from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    password_2 = serializers.CharField(
        style={'input_type': 'password'}, required=True, write_only=True
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_2'] 
        
    def save(self):
        username = self.validated_data["username"]
        email =  self.validated_data["email"]
        password = self.validated_data["password"]
        password_2 = self.validated_data["password_2"]
        if password != password_2:
            raise serializers.ValidationError("Password didn't match")
        
        user_instance = User.objects.filter(username=username, email=email)
        if user_instance.exists():
            raise serializers.ValidationError("user already exists")  
            
        user = User.objects.create(username=username, email=email)
        user.set_password(password)
        user.save()
        return user
