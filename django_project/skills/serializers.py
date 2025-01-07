from rest_framework import serializers
from .models import BackendSkill, FrontendSkill, MobileSkill


class BackendSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackendSkill
        fields = "__all__"


class FrontendSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrontendSkill
        fields = "__all__"


class MobileSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileSkill
        fields = "__all__"
