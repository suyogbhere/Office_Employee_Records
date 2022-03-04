from django.shortcuts import render,HttpResponse
from.models import *
from.forms import *
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request,'index.html')


def all_emp_page(request):
    emps = Employee.objects.all()
    context={'emps':emps}
    # print(context)
    return render(request,'allemp.html',context)

def add_emp_page(request):
    if request.method == 'POST':
        fm=Emplayeeform(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponse('Employee Added Successfully!!!!')
    else:
        fm=Emplayeeform()
    return render(request,'addemp.html',{'form':fm})



def remove_emp_page(request,emp_id=0):
    if emp_id:
        try:
            emp_remove = Employee.objects.get(id=emp_id)
            emp_remove.delete()
            return HttpResponse('Employee Removed Successfully!!!')
        except:
            return HttpResponse('Please enter A Valid EMP ID')
    emps = Employee.objects.all()
    context={'emps':emps}
    return render(request,'removemp.html',context)

def filter_emp_page(request):
    if request.method == 'POST':
        name=request.POST['name']
        dept=request.POST['dept']
        role=request.POST['role']
        emps=Employee.objects.all()
        if name:
            emps=emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps=emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)
        context={
            'emps': emps
        }
        return render(request,'allemp.html',context)

    elif request.method == 'GET':
        return render(request,'filteremp.html')
    else:
        return HttpResponse('An Exception Occured!!')

