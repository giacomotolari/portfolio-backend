import uuid
from django.db import models
from skills.models import Skill


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
        return self.project_set.all()


class EmployerCompany(Company):
    pass


class CustomerCompany(Company):
    pass
