from django.db.models import fields
from rest_framework import serializers
from ..models import Coll_UnitsModel


class Coll_UnitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coll_UnitsModel
        fields = ('totalUnits', 'unitsNames')
