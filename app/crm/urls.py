"""

"""
from django.urls import path

from crm import views

urlpatterns = [
    path("customers/", views.CustomerView.as_view({
        "get": "list",
        "post": "create"
    }), name="customers-view")
]
