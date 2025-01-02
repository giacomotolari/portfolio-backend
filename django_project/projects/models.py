# from django.db import models

# class Project(models.Model):
#     uuid = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True, unique=True)
#     name = models.CharField(max_length=255)
#     url = models.URLField(null=True, blank=True)
#     company_type = models.CharField(max_length=255, choices=TypeChoices.choices)
#     size = models.CharField(max_length=255, choices=SizeChoices.choices)

#     class Meta:
#         abstract = True

#     def __str__(self):
#         return self.name


# class EmployerCompany(Company):
#     pass


# class CustomerCompany(Company):
#     pass
