 
from rest_framework import serializers 
from .models import Drink 
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import CustomUser
  
class DrinkSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Drink 
        fields = "__all__"
        
        
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ['first_name','username','email','password']
        
        
    def create(self, validated_data):
        user = CustomUser(
            first_name=validated_data['first_name'],
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])  # This hashes the password
        user.save()
        return user
        
        

class TokenSerializer(serializers.ModelSerializer):
    """  serializer for Token model """

    user = serializers.SerializerMethodField('get_user')

    def get_user(self, obj):
        """ customize fields for Login API """

        userdata = CustomUser.objects.filter(
            id=self.instance.user.id
        ).values('id','password')

        return userdata

    class Meta:
        model = Token
        fields = ['key', 'user']
