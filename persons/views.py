from  persons.models import Person
from django.http import JsonResponse
from persons.serializers import CustomerSerializer

def persons(request):
    data = Person.objects.all()
    serializer = CustomerSerializer(data, many=True)
    return JsonResponse({'person': serializer.data})