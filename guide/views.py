from django.shortcuts import render, redirect
from django.http import Http404
from django.views import View

from guide.forms import StructurePostForm, EmployeeForm
from guide.models import Structure, Employee
from django.views.generic.base import TemplateView

from django.http import HttpResponse
import logging


logger = logging.getLogger(__name__)


def index(request):
    logger.error("Test!!")

    return HttpResponse("Hello logging world.")


class MainView(View):
    template_name = "home.html"

    def get(self, request):
        return render(request, 'guide/index.html', context={
            'structures': 'Организационная структура',
            'employes': 'Сотрудники предприятия'
        })


class StructuresView(TemplateView):
    template_name = 'guide/structures_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["structures"] = Structure.objects.all()
        return context


class StructureDetailView(View):
    def get(self, request, structure_id):
        try:
            structure = Structure.objects.get(structure_id=structure_id)
        except Exception:
            raise Http404

        context = {'structure': structure, 'form': StructurePostForm(instance=structure)}
        return render(request, 'guide/structure_detail.html', context)

    def post(self, request, structure_id):
        structure = Structure.objects.get(structure_id=structure_id)
        form = StructurePostForm(request.POST, instance=structure)
        if form.is_valid():
            application = form.save(commit=False)
            application.save()
            return redirect('structures_list')


class StructureDelete(View):
    def get(self, request, structure_id):
        try:
            structure = Structure.objects.get(structure_id=structure_id)
        except Exception:
            raise Http404
        structure.delete()
        return redirect('structures_list')


class StructureCreateView(View):
    def get(self, request):
        form = StructurePostForm()
        return render(request, 'guide/structure_create.html', {'form': form})

    def post(self, request):
        form = StructurePostForm(request.POST)
        if form.is_valid():
            structure = form.save(commit=False)
            structure.save()
            return redirect('structures_list')


class EmployeesView(TemplateView):
    template_name = 'guide/employees_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["employees"] = Employee.objects.all()
        return context


class EmployeeDetailView(View):
    def get(self, request, employee_id):
        try:
            employee = Employee.objects.get(employee_id=employee_id)
        except Exception:
            raise Http404

        context = {'employee': employee, 'form': EmployeeForm(instance=employee)}
        return render(request, 'guide/employee_detail.html', context)

    def post(self, request, employee_id):
        employee = Employee.objects.get(employee_id=employee_id)
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            application = form.save(commit=False)
            application.save()
            return redirect('employees_list')


class EmployeeDelete(View):
    def get(self, request, employee_id):
        try:
            employee = Employee.objects.get(employee_id=employee_id)
        except Exception:
            raise Http404
        employee.delete()
        return redirect('employees_list')


class EmployeeCreateView(View):
    def get(self, request):
        form = EmployeeForm()
        return render(request, 'guide/employee_create.html', {'form': form})

    def post(self, request):
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.save()
            return redirect('employees_list')
