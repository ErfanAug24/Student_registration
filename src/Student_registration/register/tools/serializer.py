from django.core import serializers


class SerializeTypes:
    def __init__(self, AnyModel):
        self.model = AnyModel

    def json_serializer(self):
        return serializers.serialize('json', self.model.objects.all())

    def xml_serializer(self):
        return serializers.serialize('xml', self.model.objects.all())

    def jsonl_serializer(self):
        return serializers.serialize('jsonl', self.model.objects.all())

    def yaml_serializer(self):
        return serializers.serialize('yaml', self.model.objects.all())
