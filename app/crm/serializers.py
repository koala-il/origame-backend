from django_countries.serializers import CountryFieldMixin
from rest_framework.serializers import ModelSerializer

from crm.models import Customer


class CustomerSerializer(CountryFieldMixin, ModelSerializer):
    # country = CountrySerializer

    class Meta:
        model = Customer
        fields = "__all__"
        read_only_fields = ("created_at", "modified_at")
