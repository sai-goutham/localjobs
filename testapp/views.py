from django.shortcuts import render
from django.db.models import Q
from django.db.models import Avg,Sum,Max,Min,Count
from testapp.models import Employee
from django.db.models.functions import Lower


# Create your views here.
def display_view(request):
    avg1=Employee.objects.all().aggregate(Avg('esal'))
    sum=Employee.objects.all().aggregate(Sum('esal'))
    max=Employee.objects.all().aggregate(Max('esal'))
    my_dict={'avg1':avg1,'sum':sum,'max':max}
    return render(request,'testapp/aggregate.html',context=my_dict)


def union(request):
    emp_list=Employee.objects.all().order_by(Lower('ename'))
    qs1=Employee.objects.filter(esal__lt=15000)
    qs2=Employee.objects.filter(ename__endswith='n')
    employees=qs1.union(qs2)
    my_dict={'emp_list':emp_list}
    return render(request,'testapp/union.html',context=my_dict)
