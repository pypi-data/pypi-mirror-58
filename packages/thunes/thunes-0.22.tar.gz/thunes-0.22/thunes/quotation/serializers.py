from rest_framework import serializers

from .models import Quotation, Destination, Source


class SourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Source
        fields = '__all__'


class DestinationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Destination
        fields = '__all__'


class QuotationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quotation
        fields = '__all__'
