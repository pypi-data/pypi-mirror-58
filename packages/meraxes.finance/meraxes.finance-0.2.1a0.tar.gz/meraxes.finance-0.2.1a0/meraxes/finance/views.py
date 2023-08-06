from rest_framework import permissions, viewsets

from meraxes.finance import models, serializer


class InstituteViewSet(viewsets.ModelViewSet):
    queryset = models.Institute.objects.order_by('name')
    serializer_class = serializer.InstituteSerializer
    permission_classes = permissions.IsAuthenticated,


class AccountViewSet(viewsets.ModelViewSet):
    queryset = models.Account.objects.order_by('institute__name', 'name')
    serializer_class = serializer.AccountSerializer
    permission_classes = permissions.IsAuthenticated,


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = models.Transaction.objects.order_by('date', 'account')
    serializer_class = serializer.TransactionSerializer
    permission_classes = permissions.IsAuthenticated,
