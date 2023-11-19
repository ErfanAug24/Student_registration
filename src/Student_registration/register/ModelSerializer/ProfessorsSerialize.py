from django.db.models import fields
from rest_framework import serializers
from ..models import ProfessorsModel


class ProfessorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessorsModel
        fields = ('nationalCode', 'professorCode', 'professorFirstName', 'professorLastName', 'professorAge',
                  'professorFathersName', 'professorMajor')
