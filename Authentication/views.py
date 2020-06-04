from django.shortcuts import render
from Authentication.models import task_user

def login(request):
    return render(request,'login.html')


def registration(request):
    if request.method=="POST":
        email = request.POST.get('mail')
        x = task_user.objects.all()
        for item in x:
            if item.email == email:
                return render(request, 'registration.html', {"error_msg": 'Mail ID is Already registered.', })
                break
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        gender = request.POST.get('gender')
        city = request.POST.get('city')
        password = request.POST.get('password')
        country = request.POST.get('country')
        obj = task_user(F_name=fname, L_name=lname, email=email, gender=gender, city=city, password=password, country=country)
        obj.save()
        return render(request, 'welcome.html')
    else:
        return render(request,'registration.html')





def check(request):
    if request.method=="POST":
        mail=request.POST.get('email')
        passwd=request.POST.get('password')
        q=task_user.objects.all()
        # print(q)
        for user in q:
            if user.email==mail:
                if  user.password==passwd:
                    request.session['msg']=user.F_name
                    request.session.set_expiry(0)
                    return render(request, 'welcome.html',{"data":user})
                    break
        else:
            return render(request,'login.html',{'error_msg':"Invalid Username or password"})
    else:
        return render(request,'login.html')
