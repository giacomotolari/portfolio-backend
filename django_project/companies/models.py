import uuid
from django.db import models


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
    url = models.URLField(null=True, blank=True)
    company_type = models.CharField(
        max_length=255, choices=TypeChoices.choices, default=TypeChoices.PRODUCT_COMPANY
    )
    size = models.CharField(max_length=255, choices=SizeChoices.choices, default=SizeChoices.MEDIUM)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class EmployerCompany(Company):
    pass


class CustomerCompany(Company):
    pass
