from django.shortcuts import render
from employee.models import Employee
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from employee.serializers import EmployeeSerializer
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

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON
    """

    def __init__(self,data,**kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/JSON'
        super(JSONResponse,self).__init__(content,**kwargs)


@csrf_exempt
def employee_list(request):
    """
    List all employees, or create a new employee
    """

    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees,many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def employee_detail(request,pk):
    """
    Retrieve, update or delete a employee.

    """
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return HttpResponse(status=404)

    if request.method=='GET':
        serializer = EmployeeSerializer(employee)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EmployeeSerializer(employee,data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)
    elif request.method=='DELETE':
        employee.delete()
        return HttpResponse(status=204)




