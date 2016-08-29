from rest_framework import serializers
from employee.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta :
        model = Employee
        fields = ('emp_id','last_name','first_name','hire_date','email_id', 'dept_id')



