from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Skill

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = "__all__"

        widgets = {
            "learned_with": FilteredSelectMultiple("Learned with", is_stacked=False),
            "skill_types": FilteredSelectMultiple("Skill type", is_stacked=False),
            "categories": FilteredSelectMultiple("Categories", is_stacked=False),
            "tool_types": FilteredSelectMultiple("Tool types", is_stacked=False),
        }
