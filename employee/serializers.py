from rest_framework import serializers
from employee.models import Employee, Department


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Department
        fields = ('dept_id','dept_name')


class EmployeeSerializer(serializers.ModelSerializer):
    dept_id = DepartmentSerializer().get_fields()

    class Meta:
        model = Employee
        fields = ('emp_id','last_name','first_name','hire_date','email_id', 'dept_id')


