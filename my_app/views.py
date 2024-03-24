import datetime

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    isActive = True
    # check=request.GET['check']
    if request.method=='POST':
        # check=request.POST['check']
        check = request.POST.get("check")
        print(check)
        if check is None: isActive=False
        else: isActive=True

    date=datetime.datetime.now()

    name="Jyoti"
    list_of_programs=['wap to check even or odd',
                      'WAP to check prime number',
                      'WAP to print all prime numbers from 1 to 100',
                      'WAP to print pascals triangle'
                      ]
    student={
        'student_name':"Rahul",
        'student_college':"XYZ",
        'student_city':"Delhi"
    }
    data={
        'date':date,
        'isActive':isActive,
        'name':name,
        'list_of_programs':list_of_programs,
        'student_data':student
    }
    # print("Home function is called in views")
    # return HttpResponse("<h1>Hello this is index page </h1>"+str(date))
    # return render(request,"home.html",{})
    return render(request, "home.html", data)
def about(request):
    print("This is About in views ")
    # return HttpResponse("<h1>This is about page</h1>")
    return render(request,"about.html", {})
def services(request):
    print("This is Services in views ")
    # return HttpResponse("<h1>This is services page</h1>")
    return render(request,"services.html",{})
