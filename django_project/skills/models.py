import uuid
from django.db import models
from multiselectfield import MultiSelectField
import datetime

year_start_learning = 2000

YEAR_CHOICES = []
for year in range(year_start_learning, (datetime.datetime.now().year + 1)):
    YEAR_CHOICES.append((year, year))


class Skill(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True, unique=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)

    started_on = models.IntegerField(
        ("year"), choices=YEAR_CHOICES, default=datetime.datetime.now().year
    )
    last_used_on = models.IntegerField(
        ("year"), choices=YEAR_CHOICES, default=datetime.datetime.now().year
    )

    class LearnedWithChoices(models.TextChoices):
        COURSES = "courses"
        PRACTICE = "practice"
        EXERCISES = "exercises"
        PROJECTS = "projects"
        BOOKS = "books"
        TUTORIALS = "tutorials"
        DOCUMENTATIONS = "documentations"
        MENTORS = "mentors"
        AI_BOTS = "ai bots"
        OTHER = "other"

    learned_with = MultiSelectField(
        choices=LearnedWithChoices.choices,
        null=True,
        blank=True,
        help_text="Indicate with which tools or methods you learned this skill.",
    )

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

    @property
    def projects(self):
        return self.project_set.all()

    @property
    def companies(self):
        return self.company_set.all()


class DevelopmentSkill(Skill):
    class LevelChoices(models.TextChoices):
        BEGINNER = "beginner"
        INTERMEDIATE = "intermediate"
        EXPERT = "expert"
        MASTER = "master"

    level = models.CharField(max_length=50, choices=LevelChoices.choices, null=True, blank=False)

    class TypeChoices(models.TextChoices):
        LANGUAGE = "language"
        FRAMEWORK = "framework"
        LIBRARY = "library"
        TOOL = "tool"

    skill_type = models.CharField(max_length=50, choices=TypeChoices, null=True, blank=True)

    class ToolTypeChoices(models.TextChoices):
        IDE = "ide"
        EDITOR = "editor"
        CI_CD = "CI/CD"
        CONTAINERIZATION = "containerization"
        MONITORING = "monitoring"
        LOGGING = "logging"
        TESTING = "testing"
        DEBUGGING = "debugging"

    tool_type = models.CharField(max_length=50, choices=ToolTypeChoices.choices, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.skill_type == self.TypeChoices.TOOL and not self.tool_type:
            raise ValueError("tool_type must be set if skill_type is 'tool'")
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class BackendSkill(DevelopmentSkill):
    class CategoryChoices(models.TextChoices):
        DATA_BASE = "database"
        DEVOPS = "devops"
        SERVER = "server"
        CLOUD = "cloud"
        SECURITY = "security"

    category = models.CharField(max_length=50, choices=CategoryChoices.choices, null=True, blank=True)


class FrontendSkill(DevelopmentSkill):
    class CategoryChoices(models.TextChoices):
        STYLE = "style"
        UI = "ui"
        UX = "ux"
        LOGIC = "logic"

    category = models.CharField(max_length=50, choices=CategoryChoices.choices, null=True, blank=True)


class MobileSkill(DevelopmentSkill):
    class CategoryChoices(models.TextChoices):
        ANDROID = "android"
        IOS = "ios"
        CROSS_PLATFORM = "cross-platform"

    category = models.CharField(max_length=50, choices=CategoryChoices.choices, null=True, blank=True)


class LanguageSkill(Skill):
    class LanguageLevelChoices(models.TextChoices):
        BASIC = "basic"
        FLUENT = "fluent"
        INTERMEDIATE = "intermediate"
        NATIVE = "native"

    level = models.CharField(max_length=50, choices=LanguageLevelChoices.choices, null=True, blank=False)
