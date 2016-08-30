from django.shortcuts import render
from employee.models import Employee, Department
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from employee.serializers import EmployeeSerializer, DepartmentSerializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def search(request):
    errors = []
    if 'q' in request.GET :
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term')
        else:
            employee = Employee.objects.filter(last_name__icontains=q)
            return render(request, 'search_requests.html',
                      {'employee':employee, 'query':q})

    return render(request, 'search_form.html', {'errors': errors})


@api_view(['GET','POST'])
def employee_list(request, format=None):
    """
    List all employees, or create a new employee
    """

    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def employee_detail(request, pk, format=None):
    """
    Retrieve, update or delete a employee.

    """
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EmployeeSerializer(employee,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
def department_list(request,format=None):
    """
    List all departments
    """
    if request.method == 'GET':
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def department_detail(request, pk, format=None):
    """
    Retrieve, update or delete a department

    """
    try:
        department = Department.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = Department(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        department.delet()
        return Response(status=status.HTTP_204_NO_CONTENT)








