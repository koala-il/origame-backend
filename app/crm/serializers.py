from rest_framework.serializers import ModelSerializer

from crm.models import Customer


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            "id"
        )
