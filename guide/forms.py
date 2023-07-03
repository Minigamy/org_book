from django import forms

from .models import Structure, Employee


class StructurePostForm(forms.ModelForm):
    class Meta:
        model = Structure
        fields = ('idup', 'name',)


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('orgid', 'name', 'old')



