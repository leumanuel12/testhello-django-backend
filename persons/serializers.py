from rest_framework import serializers
from persons.models import Person
from django.contrib.auth.models import User

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    def create(self, validate_data):
        user = User.objects.create(
            username=validate_data['username'],
            email=validate_data['email']
        )

        user.set_password(validate_data['password'])
        user.save()
        return user