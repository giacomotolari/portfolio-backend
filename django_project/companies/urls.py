from django.urls import path
from . import views

urlpatterns = [
    path("employers/", views.employers, name="companies.employers"),
    path("customers/", views.customers, name="companies.customers"),
]
