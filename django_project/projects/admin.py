from django.contrib import admin

from .models import PersonalProject, AsEmployeeProject, TeamOpenSourceProject, TeamPrivateProject

admin.site.register(PersonalProject)
admin.site.register(AsEmployeeProject)
admin.site.register(TeamOpenSourceProject)
admin.site.register(TeamPrivateProject)
