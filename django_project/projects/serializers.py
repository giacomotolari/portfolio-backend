from rest_framework import serializers
from .models import AsEmployeeProject, PersonalProject, TeamPrivateProject, TeamOpenSourceProject
from skills.serializers import BackendSkillSerializer, FrontendSkillSerializer, MobileSkillSerializer
# from companies.serializers import CustomerCompanySerializer


class AsEmployeeProjectSerializer(serializers.ModelSerializer):
    backend_stack = BackendSkillSerializer(many=True)
    frontend_stack = FrontendSkillSerializer(many=True)
    mobile_stack = MobileSkillSerializer(many=True)
    # customer_companies = CustomerCompanySerializer(many=True)

    class Meta:
        model = AsEmployeeProject
        exclude = ("id", "employed_by")


class PersonalProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalProject
        exclude = ("id",)


class TeamOpenSourceProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamOpenSourceProject
        exclude = ("id",)


class TeamPrivateProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamPrivateProject
        exclude = ("id",)
