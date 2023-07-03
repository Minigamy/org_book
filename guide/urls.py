from django.urls import path
from .views import StructuresView, StructureDetailView, StructureDelete, StructureCreateView, MainView, EmployeesView, \
    EmployeeDetailView, EmployeeDelete, EmployeeCreateView

urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('structures/', StructuresView.as_view(), name='structures_list'),
    path('structure/<int:structure_id>/', StructureDetailView.as_view(), name='structure_details'),
    path('structure/delete/<int:structure_id>/', StructureDelete.as_view(), name='structure_delete'),
    path('structure/create/', StructureCreateView.as_view(), name='structure_create'),

    path('employees/', EmployeesView.as_view(), name='employees_list'),
    path('employees/<int:employee_id>/', EmployeeDetailView.as_view(), name='employee_details'),
    path('employee/delete/<int:employee_id>/', EmployeeDelete.as_view(), name='employee_delete'),
    path('employee/create/', EmployeeCreateView.as_view(), name='employee_create'),
]

