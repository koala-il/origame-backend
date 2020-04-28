from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from crm.models import Customer
from crm.serializers import CustomerSerializer


class CustomerView(ModelViewSet):
    serializer_class = CustomerSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """
        We want the user to get only the Customers associated with his account.
        """
        user = self.request.user

        return Customer.objects.filter(user=user).order_by("first_name")
