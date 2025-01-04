from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Skill


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = "__all__"

        widgets = {
            "learned_with": FilteredSelectMultiple("Learned with", is_stacked=False),
            # "started_on": forms.DateInput(attrs={"type": "month"}),  
            # "last_used_on": forms.DateInput(attrs={"type": "month"}),  
        }
