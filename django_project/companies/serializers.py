from rest_framework import serializers
from .models import EmployerCompany, CustomerCompany
from skills.serializers import BackendSkillSerializer, FrontendSkillSerializer, MobileSkillSerializer
from projects.serializers import AsEmployeeProjectSerializer
from rest_framework import serializers

class EmployerCompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = EmployerCompany
        exclude = ("id",)

    backend_skills = serializers.SerializerMethodField()
    frontend_skills = serializers.SerializerMethodField()
    mobile_skills = serializers.SerializerMethodField()
    projects = serializers.SerializerMethodField()

    def get_backend_skills(self, obj):
        return BackendSkillSerializer(obj.backend_skills, many=True).data

    def get_frontend_skills(self, obj):
        return FrontendSkillSerializer(obj.frontend_skills, many=True).data

    def get_mobile_skills(self, obj):
        return MobileSkillSerializer(obj.mobile_skills, many=True).data

    def get_projects(self, obj):
        return AsEmployeeProjectSerializer(obj.projects, many=True).data


class CustomerCompanySerializer(serializers.ModelSerializer):
    backend_skills = serializers.SerializerMethodField()
    frontend_skills = serializers.SerializerMethodField()
    mobile_skills = serializers.SerializerMethodField()
    projects = serializers.SerializerMethodField()

    class Meta:
        model = CustomerCompany
        exclude = ("id",)

    def get_backend_skills(self, obj):
        return BackendSkillSerializer(obj.backend_skills, many=True).data

    def get_frontend_skills(self, obj):
        return FrontendSkillSerializer(obj.frontend_skills, many=True).data

    def get_mobile_skills(self, obj):
        return MobileSkillSerializer(obj.mobile_skills, many=True).data

    def get_projects(self, obj):
        return AsEmployeeProjectSerializer(obj.projects, many=True).data
