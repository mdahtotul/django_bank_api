import random
from rest_framework import status
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.response import Response
from bank.models import Account, Address, Bank, Branch
from bank.permissions import IsAdmin, IsAdminOrReadOnly, IsManager, IsManagerOrReadOnly
from bank.serializers import (
    AccountSerializer,
    AddressSerializer,
    BankSerializer,
    BranchSerializer,
    CreateAccountSerializer,
    CreateBranchSerializer,
    UpdateAccountSerializer,
    UpdateBranchSerializer,
)


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class BankViewSet(ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class BranchViewSet(ModelViewSet):
    queryset = Branch.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreateBranchSerializer
        elif self.request.method == "PUT":
            return UpdateBranchSerializer
        else:
            return BranchSerializer

    def create(self, request, *args, **kwargs):
        random_number = random.randint(1, 10000)
        route_no = f"{202300000 + random_number}"
        serializer = CreateBranchSerializer(
            data=request.data, context={"routing_no": route_no}
        )
        serializer.is_valid(raise_exception=True)
        branch = serializer.save()

        serializer = BranchSerializer(branch)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AccountViewSet(ModelViewSet):
    queryset = Account.objects.all()
    permission_classes = [IsManagerOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreateAccountSerializer
        elif self.request.method == "PUT":
            return UpdateAccountSerializer
        else:
            return AccountSerializer

    def create(self, request, *args, **kwargs):
        random_number = random.randint(1, 100000)
        u_no = f"{10000000 + random_number}"
        serializer = CreateAccountSerializer(data=request.data, context={"u_no": u_no})
        serializer.is_valid(raise_exception=True)
        account = serializer.save()

        serializer = AccountSerializer(account)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
