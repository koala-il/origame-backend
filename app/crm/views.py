# Create your views here.
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.viewsets import ModelViewSet

from crm.serializers import CustomerSerializer


class CustomerView(ModelViewSet):
    serializer_class = CustomerSerializer

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "name": openapi.Schema(type=openapi.TYPE_STRING),
                "phone": openapi.Schema(type=openapi.TYPE_STRING),
                "email": openapi.Schema(type=openapi.TYPE_STRING),
            },
        )
    )
    def list(self, request, *args, **kwargs):
        return super(self).list(request, *args, **kwargs)
