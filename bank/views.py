import random
from rest_framework import status
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.response import Response
from bank.models import Account, Address, Bank, Branch
from bank.serializers import (
    AccountSerializer,
    AddressSerializer,
    BankSerializer,
    BranchSerializer,
    CreateBranchSerializer,
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
    serializer_class = AccountSerializer
