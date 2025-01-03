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
                "fields": (
                    "web_page",
                    "git_hub",
                    "git_lab",
                    "play_store",
                    "app_store",
                    "image",
                    "video",
                    "other",
                ),
            },
        ),
        (
            None,
            {
                "fields": ("goals", "extra_infos"),
            },
        ),
    )
    list_display = ("name", "start_date", "end_date", "status", "size")
    list_filter = ("status", "categories", "runs_on", "size")
    search_fields = ("name", "uuid")


@admin.register(AsEmployeeProject)
class AsEmployeeProjectAdmin(ProjectAdmin):
    fieldsets = ProjectAdmin.fieldsets + (
        (
            "Companies",
            {
                "fields": ("employed_by", "customer_companies"),
            },
        ),
    )
    list_display = ProjectAdmin.list_display + ("employed_by",)
    search_fields = ProjectAdmin.search_fields + ("employed_by", "customer_companies")


admin.site.register(PersonalProject, ProjectAdmin)
admin.site.register(TeamPrivateProject, ProjectAdmin)
admin.site.register(TeamOpenSourceProject, ProjectAdmin)
