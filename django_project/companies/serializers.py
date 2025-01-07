from rest_framework import serializers
from .models import EmployerCompany, CustomerCompany


class EmployerCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployerCompany
        fields = "__all__"


class CustomerCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerCompany
        fields = "__all__"
