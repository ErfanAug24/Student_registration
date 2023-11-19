from django.db import models
from django.utils import timezone
from .tools.serializer import SerializeTypes


class CollegianModel(models.Model):
    nationalCode = models.CharField(max_length=10, null=False)
    collegianCode = models.CharField(max_length=14, null=False)
    collegianFirstName = models.CharField(max_length=200, null=False)
    collegianLastName = models.CharField(max_length=300, null=False)
    collegianAge = models.IntegerField(default=18)
    collegianFathersName = models.CharField(max_length=400, null=False)
    collegianMajor = models.CharField(max_length=200, null=False)
    pub_date = models.DateTimeField(default=timezone.now)
    rm_date = models.DateTimeField(default=timezone.now)
    coll_units = models.ManyToManyField('Coll_UnitsModel')

    def __init__(self, nationalCode, collegianCode, collegianFirstName, collegianLastName, collegianAge,
                 collegianFathersName, collegianMajor, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nationalCode = nationalCode
        self.collegianCode = collegianCode
        self.collegianFirstName = collegianFirstName
        self.collegianLastName = collegianLastName
        self.collegianAge = collegianAge
        self.collegianFathersName = collegianFathersName
        self.collegianMajor = collegianMajor

    def __str__(self):
        return SerializeTypes(AnyModel=CollegianModel).json_serializer()

    @classmethod
    def find_by_name(cls, name) -> "CollegianModel":
        return cls.objects.get(collegianFirstName=name)

    def find_by_id(cls, id) -> "CollegianModel":
        return cls.objects.get(pk=id)

    def save(self):
        pass


class Coll_UnitsModel(models.Model):
    totalUnits = models.IntegerField(default=0)
    unitsNames = models.CharField(max_length=400, null=False)
    pub_date = models.DateTimeField(default=timezone.now)
    rm_date = models.DateTimeField(default=timezone.now)
    professors = models.ManyToManyField('ProfessorsModel')

    def __str__(self):
        return SerializeTypes(Coll_Units).json_serializer()


class ProfessorsModel(models.Model):
    nationalCode = models.CharField(max_length=10, null=False)
    professorCode = models.CharField(max_length=14, null=False)
    professorFirstName = models.CharField(max_length=200, null=False)
    professorLastName = models.CharField(max_length=300, null=False)
    professorAge = models.IntegerField(default=28)
    professorFathersName = models.CharField(max_length=400, null=False)
    professorMajor = models.CharField(max_length=200, null=False)
    pub_date = models.DateTimeField(default=timezone.now)
    rm_date = models.DateTimeField(default=timezone.now)
    collegians = models.ManyToManyField('CollegianModel')

    def __str__(self):
        return SerializeTypes(Professors).json_serializer()
