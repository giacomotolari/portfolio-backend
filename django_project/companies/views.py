from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import EmployerCompany, CustomerCompany
from .serializers import EmployerCompanySerializer, CustomerCompanySerializer

@api_view(['GET'])
def employers(request):
    print('request:', request)
    employers = EmployerCompany.objects.all()
    serializer = EmployerCompanySerializer(employers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def customers(request):
    print('request:', request)
    customers = CustomerCompany.objects.all()
    serializer = CustomerCompanySerializer(customers, many=True)
    return Response(serializer.data)