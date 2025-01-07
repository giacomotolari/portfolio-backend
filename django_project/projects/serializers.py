from rest_framework import serializers
from .models import AsEmployeeProject, PersonalProject, TeamPrivateProject, TeamOpenSourceProject


class AsEmployeeProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsEmployeeProject
        fields = "__all__"


class PersonalProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalProject
        fields = "__all__"


class TeamOpenSourceProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamOpenSourceProject
        fields = "__all__"


class TeamPrivateProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamPrivateProject
        fields = "__all__"
