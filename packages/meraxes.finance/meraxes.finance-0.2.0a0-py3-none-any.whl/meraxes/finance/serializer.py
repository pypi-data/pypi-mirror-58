from rest_framework import serializers

from meraxes.finance import models


class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Institute
        fields = (
            'id',
            'name',
        )


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        fields = (
            'id',
            'institute',
            'name',
        )


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transaction
        fields = (
            'account',
            'amount',
            'currency',
            'date',
            'purpose'
        )
