"""external/internal imports"""
from rest_framework import serializers
from bank.models import Account, Bank, Address, Branch


""" Serializers """


class SimpleAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ["id", "details", "zip_code", "city"]


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ["id", "details", "state", "zip_code", "city", "country"]


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ["id", "name", "code"]


class SimpleBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ["id", "name", "routing_no", "phone"]


class BranchSerializer(serializers.ModelSerializer):
    address = SimpleAddressSerializer()

    class Meta:
        model = Branch
        fields = ["id", "name", "routing_no", "address", "phone"]


class CreateBranchSerializer(serializers.ModelSerializer):
    def save(self, **kwargs):
        routing_no = self.context.get("routing_no")
        self.instance = Branch.objects.create(
            routing_no=routing_no, **self._validated_data
        )
        return self.instance

    class Meta:
        model = Branch
        fields = ["id", "name", "address", "phone"]


class UpdateBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ["id", "name", "address", "phone"]


class AccountSerializer(serializers.ModelSerializer):
    branch = SimpleBranchSerializer()
    address = SimpleAddressSerializer()

    class Meta:
        model = Account
        fields = [
            "id",
            "UNO",
            "type",
            "phone",
            "bod",
            "balance",
            "user",
            "branch",
            "address",
        ]


class CreateAccountSerializer(serializers.ModelSerializer):
    def save(self, **kwargs):
        UNO = self.context.get("u_no")
        self.instance = Account.objects.create(UNO=UNO, **self._validated_data)
        return self.instance

    class Meta:
        model = Account
        fields = ["id", "type", "phone", "bod", "balance", "user", "branch", "address"]


class UpdateAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["id", "type", "phone", "bod", "balance", "address"]
