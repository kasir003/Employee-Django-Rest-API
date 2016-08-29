from django.contrib import admin
from employee.models import Department,Employee,Salary
# Register your models here.

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Salary)