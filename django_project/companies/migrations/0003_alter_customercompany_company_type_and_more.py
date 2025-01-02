# Generated by Django 5.1.2 on 2025-01-02 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("companies", "0002_customercompany_size_employercompany_size_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customercompany",
            name="company_type",
            field=models.CharField(
                choices=[
                    ("product-company", "Product Company"),
                    ("agency", "Agency"),
                    ("school", "School"),
                ],
                max_length=255,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="employercompany",
            name="company_type",
            field=models.CharField(
                choices=[
                    ("product-company", "Product Company"),
                    ("agency", "Agency"),
                    ("school", "School"),
                ],
                max_length=255,
                null=True,
            ),
        ),
    ]
