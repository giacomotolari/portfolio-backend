from rest_framework import serializers
from .models import BackendSkill, FrontendSkill, MobileSkill

class BackendSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackendSkill
        exclude = ("id",)


class FrontendSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrontendSkill
        exclude = ("id",)


class MobileSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileSkill
        exclude = ("id",)
