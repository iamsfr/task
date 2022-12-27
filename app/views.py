from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def loginAction(request):
    username=request.POST['username']
    password=request.POST['password']
    user=Register.objects.filter(username=username,password=password)
    if user.count()>0:
        request.session['id']=user[0].id
        return render(request,"userhome.html",{'data':user})
    else:
         messages.add_message(request,messages.INFO,"incorrect username")
         return redirect('login')

def registerAction(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already taken")
                return redirect('register')
            else:
                user = Register(username=username, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,"password mismatch")
            return redirect('register')
        return redirect('/')
    return render(request, 'register.html')

def form(request):
    district = District.objects.all()
    branch = Branch.objects.all()
    return render(request, 'form.html',{'district':district, 'branch':branch})

def getbranch(request):
    cid = request.GET['district_id']
    branch = Branch.objects.filter(branchid=cid)
    return render(request,'getbranch.html',{'branch':branch})

def logout(request):
    request.session.flush()
    messages.add_message(request,messages.INFO,'Logout success')
    return redirect('login')

def formAction(request):
    userid = request.session['id']
    name = request.POST['name']
    address = request.POST['address']
    age = request.POST['age']
    email = request.POST['email']
    gender = request.POST['gender']
    district = request.POST['district']
    branch = request.POST['branch']
    phone = request.POST['phone']
    account = request.POST['account']
    user = Form(userid_id=userid,name=name, address=address,age=age, email=email, gender=gender, district_id=district, branch_id=branch, phone=phone, account=account)
    user.save()
    messages.add_message(request,messages.INFO,"application accepted")
    return redirect('form')
def viewform(request):
    userid = request.session['id']
    user = Form.objects.filter(userid=userid)
    return render(request,'viewform.html',{'user':user})