import uuid
from django.db import models
from projects.models import Project


class TypeChoices(models.TextChoices):
    PRODUCT_COMPANY = ("product-company", "Product Company")
    AGENCY = ("agency", "Agency")
    SCHOOL = ("school", "School")


class SizeChoices(models.TextChoices):
    SMALL = "small"
    MEDIUM = "medium"
    BIG = "big"
    VERY_BIG = ("very-big", "Very big")


class Company(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True, unique=True)
    name = models.CharField(max_length=255)
    company_type = models.CharField(max_length=255, choices=TypeChoices.choices, null=True, blank=False)
    size = models.CharField(max_length=255, choices=SizeChoices.choices, default=SizeChoices.MEDIUM)
    url = models.URLField(null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    @property
    def projects(self):
        if hasattr(Project, "_meta") and Project._meta.abstract:
            raise ValueError("Cannot fetch projects for an abstract class.")
        return Project.objects.filter(models.Q(employed_by=self) | models.Q(customer_companies=self))


class EmployerCompany(Company):
    def backend_skills(self):
        """Fetch backend skills based on projects related to the company."""
        return {skill for project in self.projects for skill in project.backend_stack.all()}

    def frontend_skills(self):
        """Fetch frontend skills based on projects related to the company."""
        return {skill for project in self.projects for skill in project.frontend_stack.all()}

    def mobile_skills(self):
        """Fetch mobile skills based on projects related to the company."""
        return {skill for project in self.projects for skill in project.mobile_stack.all()}


class CustomerCompany(Company):
    def backend_skills(self):
        """Fetch backend skills based on projects related to the company."""
        return {skill for project in self.projects for skill in project.backend_stack.all()}

    def frontend_skills(self):
        """Fetch frontend skills based on projects related to the company."""
        return {skill for project in self.projects for skill in project.frontend_stack.all()}

    def mobile_skills(self):
        """Fetch mobile skills based on projects related to the company."""
        return {skill for project in self.projects for skill in project.mobile_stack.all()}
