from rest_framework import serializers
from .models import Encroachment, Area


class EncroachmentSerializer(serializers.Serializer):
    encroachment_id = serializers.CharField(max_length=255)
    encroachment_type = serializers.CharField(max_length=255)
    encroachment_size_sq_ft = serializers.DecimalField(max_digits=10, decimal_places=2)
    criticality = serializers.CharField(max_length=255)
    encroachment_department = serializers.CharField(max_length=200)
    encroachment_status=serializers.CharField(max_length=200)
    distance_from_center_ft = serializers.IntegerField()
    area=serializers.RelatedField(source="Area",read_only=True)

    def create(self, validated_data):
        return Encroachment.objects.create(**validated_data)
    

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance