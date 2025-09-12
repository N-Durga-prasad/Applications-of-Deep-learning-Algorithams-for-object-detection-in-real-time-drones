from django.shortcuts import render
from django.contrib import messages
from User.models import UserRegister
# Create your views here.

def AdminLogin(request):
    if request.method=='POST':
        username= request.POST['username']
        password = request.POST['password']
        if username=='admin' and password=='admin':
            return render(request, 'Admins/adminhome.html' )
        else:
            messages.success(request , 'Invalid Credintals--')
    return render(request , 'adminlogin.html')

def adminhome(request):
    return render(request , 'Admins/adminhome.html')

def viewusers(request):
    data= UserRegister.objects.all()
    return render(request , 'Admins/viewusers.html' , {'data' : data})

def Activateuser(request):
     if request.method=='GET':
         id = request.GET.get('uid')
         Status= "Activated"
         UserRegister.objects.filter(id=id).update(Status=Status)
         data = UserRegister.objects.all()
     return render(request , 'Admins/viewusers.html' , {'data' :data})
 
def DeleteUser(request):
     if request.method=='GET':
         id = request.GET.get('uid')
         UserRegister.objects.get(id=id).delete()
         data= UserRegister.objects.all()
     return render(request , 'Admins/viewusers.html' , {'data' : data})
         