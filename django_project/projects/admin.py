from django.contrib import admin

from .models import PersonalProject, AsEmployeeProject, TeamOpenSourceProject, TeamPrivateProject
from .forms import ProjectUrlsForm


class ProjectAdmin(admin.ModelAdmin):
    form = ProjectUrlsForm
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "description",
                    "status",
                    "size",
                    "start_date",
                    "end_date",
                    "runs_on",
                    "categories",
                )
            },
        ),
        (
            "Project URLs",
            {
                "fields": ("web_page", "git_hub", "git_lab", "play_store", "app_store", "other"),
            },
        ),
        (
            None,
            {
                "fields": ("goals", "extra_infos"),
            },
        ),
    )


@admin.register(AsEmployeeProject)
class AsEmployeeProjectAdmin(ProjectAdmin):
    list_display = ("name", "employed_by", "start_date", "end_date", "status")
    list_filter = ("employed_by", "status", "categories")
    search_fields = ("name", "employed_by__name")


admin.site.register(PersonalProject, ProjectAdmin)
admin.site.register(TeamPrivateProject, ProjectAdmin)
admin.site.register(TeamOpenSourceProject, ProjectAdmin)
