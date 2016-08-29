from django.db import models
import datetime


# Create your models here.

class Department(models.Model):
    dept_id = models.CharField(max_length=10, primary_key=True)
    dept_name = models.CharField(max_length=30)

    def __str__(self):
        return self.dept_name

    class Meta:
        ordering = ('dept_id',)


class Employee(models.Model):
    first_name = models.CharField(max_length=30,blank=True)
    last_name = models.CharField(max_length=30)
    emp_id = models.AutoField(primary_key=True)
    hire_date = models.DateField(default=datetime.date.today)
    email_id = models.EmailField(blank=True)
    dept = models.ForeignKey(Department)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        ordering = ('emp_id',)


class Salary(models.Model):
    emp_id = models.ForeignKey(Employee)
    salary = models.IntegerField()
    from_date = models.DateField()
    to_date = models.DateField()

    def __str__(self):
        return self.salary

    class Meta:
        ordering = ('emp_id',)
