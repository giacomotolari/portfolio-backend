import uuid
from django.db import models
from companies.models import EmployerCompany, CustomerCompany
from multiselectfield import MultiSelectField

class ContributionRoleChoices(models.TextChoices):
    FRONTEND_DEVELOPER = "Frontend Developer"
    FULL_STACK_DEVELOPER = "Full Stack Developer"
    BACKEND_DEVELOPER = "Backend Developer"
    ANDROID_DEVELOPER = "Android Developer"
    IOS_DEVELOPER = "iOS Developer"
    CROSS_PLATFORM_DEVELOPER = "Cross-Platform Developer"
    DEVOPS = "DevOps"


class Project(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    class StatusChoices(models.TextChoices):
        PLANNED = "planned"
        IN_PROGRESS = "in progress"
        MAINTAINED = "maintained"
        COMPLETED = "completed"
        ARCHIVED = "archived"
        PAUSED = "paused"

    status = models.CharField(max_length=50, choices=StatusChoices.choices, null=True, blank=False)

    class SizeChoices(models.TextChoices):
        SMALL = "small"
        MEDIUM = "medium"
        BIG = "big"
        VERY_BIG = "very big"

    size = models.CharField(max_length=50, choices=SizeChoices.choices, null=True, blank=False)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    class RunsOnChoices(models.TextChoices):
        WEB = "web"
        DESKTOP = "desktop"
        IOS = "ios"
        ANDROID = "android"

    runs_on = MultiSelectField(
        choices=RunsOnChoices.choices,
        null=True,
        blank=False,
        max_length=255,
    )

    class GoalsChoices(models.TextChoices):
        LEARNING = "learning"
        EARN_MONEY = "earn money"
        SHOWCASING = "showcasing"

    goals = MultiSelectField(
        choices=GoalsChoices.choices,
        null=True,
        blank=False,
        max_length=255,
    )

    class CategoriesChoices(models.TextChoices):
        E_COMMERCE = "e-commerce"
        LOGISTICS = "logistics"
        COMMUNITY = "community"
        GAME = "game"
        PORTFOLIO = "portfolio"
        BLOG = "blog"
        OTHER = "other"

    categories = MultiSelectField(
        choices=CategoriesChoices.choices,
        null=True,
        blank=False,
        max_length=255,
    )

    backend_stack = models.ManyToManyField(
        "skills.BackendSkill", related_name="projects", null=True, blank=True
    )
    frontend_stack = models.ManyToManyField(
        "skills.FrontendSkill", related_name="projects", null=True, blank=True
    )
    mobile_stack = models.ManyToManyField(
        "skills.MobileSkill", related_name="projects", null=True, blank=True
    )

    urls = models.JSONField(null=True, blank=True)
    extra_infos = models.TextField(null=True, blank=True, max_length=255)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class AsEmployeeProject(Project):
    employed_by = models.ForeignKey(EmployerCompany, null=False, blank=False, on_delete=models.CASCADE)
    customer_companies = models.ManyToManyField(CustomerCompany, related_name="projects")


class PersonalProject(Project):
    pass


class TeamPrivateProject(Project):
    pass


class TeamOpenSourceProject(Project):
    pass
