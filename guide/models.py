from django.db import models


class Structure(models.Model):
    structure_id = models.IntegerField(primary_key=True, auto_created=True, unique=True)
    idup = models.IntegerField(blank=True, null=True)
    name = models.TextField()

    def __str__(self):
        return self.name


class Employee(models.Model):
    employee_id = models.IntegerField(primary_key=True, auto_created=True, unique=True)
    orgid = models.ForeignKey(Structure, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    old = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
