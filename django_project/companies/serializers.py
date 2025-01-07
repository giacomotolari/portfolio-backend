from rest_framework import serializers
from .models import EmployerCompany, CustomerCompany
from skills.serializers import BackendSkillSerializer, FrontendSkillSerializer, MobileSkillSerializer
from rest_framework import serializers


class EmployerCompanySerializer(serializers.ModelSerializer):
    backend_skills = serializers.SerializerMethodField()
    frontend_skills = serializers.SerializerMethodField()
    mobile_skills = serializers.SerializerMethodField()
    # projects = serializers.SerializerMethodField()

    class Meta:
        model = EmployerCompany
        fields = "__all__"

    def get_backend_skills(self, obj):
        return BackendSkillSerializer(obj.backend_skills, many=True).data

    def get_frontend_skills(self, obj):
        return FrontendSkillSerializer(obj.frontend_skills, many=True).data

    def get_mobile_skills(self, obj):
        return MobileSkillSerializer(obj.mobile_skills, many=True).data

    # def get_projects(self, obj):
    #     return list(obj.projects)


class CustomerCompanySerializer(serializers.ModelSerializer):
    backend_skills = serializers.SerializerMethodField()
    frontend_skills = serializers.SerializerMethodField()
    mobile_skills = serializers.SerializerMethodField()
    # projects = serializers.SerializerMethodField()

    class Meta:
        model = CustomerCompany
        fields = "__all__"

    def get_backend_skills(self, obj):
        return BackendSkillSerializer(obj.backend_skills, many=True).data

    def get_frontend_skills(self, obj):
        return FrontendSkillSerializer(obj.frontend_skills, many=True).data

    def get_mobile_skills(self, obj):
        return MobileSkillSerializer(obj.mobile_skills, many=True).data

    # def get_projects(self, obj):
    #     return list(obj.projects)
