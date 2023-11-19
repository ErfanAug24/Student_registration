from django.db.models import fields
from rest_framework import serializers
from ..models import CollegianModel


class CollegianSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollegianModel
        fields = ('nationalCode', 'collegianCode', 'collegianFirstName', 'collegianLastName', 'collegianAge',
                  'collegianFathersName', 'collegianMajor')
