from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Emp,Testimonial
from .form import FeedBackForm,EmpForm

# Create your views here.

def emp_home(request):
    emps=Emp.objects.all()
    return render(request, "emp/home.html", {
        'emps':emps
    })

    # return HttpResponse("Student Home page")
    # return render(request,"emp/home.html",{})

def add_emp(request):
    if request.method=="POST":
        # print("Data is coming")

        # 1. data fetch
        emp_name=request.POST.get("emp_name")
        emp_id=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_dept=request.POST.get("emp_department")

        #Validation

        # 2. create model object and set data
        e=Emp()

        e.name=emp_name
        e.emp_id=emp_id
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_dept

        if emp_working is None:
            e.working=False
        else:
            e.working=True

        # 3. save the object
        e.save()

        # 4. prepare msg

        return redirect("/emp/home/")
    form=EmpForm()
    form.save()
    return render(request,"emp/add_emp.html",{'form':form})


def delete_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    emp.delete()
    # print(emp_id)
    return redirect("/emp/home/")

def update_emp(request, emp_id):
    emp=Emp.objects.get(pk=emp_id)
    return render(request,"emp/update_emp.html",{
        'emp':emp
    })


def do_update_emp(request,emp_id):
    if request.method=="POST":
        emp_name = request.POST.get("emp_name")
        emp_id_temp = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working")
        emp_dept = request.POST.get("emp_department")

        e=Emp.objects.get(pk=emp_id)
        e.name = emp_name
        e.emp_id = emp_id_temp
        e.phone = emp_phone
        e.address = emp_address
        e.department = emp_dept
        if emp_working is None:
            e.working=False
        else:
            e.working=True
        e.save()

    return redirect("/emp/home")

def testimonials(request):
    testi=Testimonial.objects.all()

    return render(request,"emp/testimonials.html",{
        'testi':testi
    })

def feedback(request):
    if request.method=='POST':
        form=FeedBackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['email'])
            # form.save()
            print("Data saved")
        else:
            return render(request, "emp/feedback.html", {'form': form})


    else:
        form=FeedBackForm()
        return render(request,"emp/feedback.html",{'form':form})
