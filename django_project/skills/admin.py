from django.contrib import admin
from .models import BackendSkill, FrontendSkill, LanguageSkill, MobileSkill
from .forms import SkillForm


class SkillAdmin(admin.ModelAdmin):
    form = SkillForm


# developer
admin.site.register(FrontendSkill, SkillAdmin)
admin.site.register(MobileSkill, SkillAdmin)
admin.site.register(BackendSkill, SkillAdmin)

# other
admin.site.register(LanguageSkill, SkillAdmin)
