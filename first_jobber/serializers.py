from rest_framework import serializers
from .models import Insurance, User, Coverage

class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = ('name', 'insurance_class', 'price')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'name', 'password')

class CoverageSerializer(serializers.ModelSerializer):
    insuranceId = InsuranceSerializer()

    class Meta:
        model = Coverage
        fields = ('insuranceId', 'car', 'medicine', 'third_party', 'lost')

    def create(self, validated_data):
        insurance_data = validated_data.pop('insuranceId')
        insurance_serializer = InsuranceSerializer(data=insurance_data)
        if insurance_serializer.is_valid():
            insurance = insurance_serializer.save()
            coverage = Coverage.objects.create(insuranceId=insurance, **validated_data)
            return coverage
        else:
            raise serializers.ValidationError(insurance_serializer.errors)
