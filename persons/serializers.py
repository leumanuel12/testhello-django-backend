from rest_framework import serializers
from persons.models import Person

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'