from django.shortcuts import render,HttpResponse,redirect
from  django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import user_otp
from django.core.mail import send_mail
from django.conf import settings
import random

#sending mail
def sent(receiver,otp):
    msg = "Your otp is \n"+otp 
    subject= "One time password"
    sender = settings.EMAIL_HOST_USER
    send_mail(subject,msg, sender,[receiver],fail_silently=False)
    

# Create your views here.
def signup(request):
    if request.method=='POST':
       username=request.POST['username']
       email=request.POST['email']
       password=request.POST['password']
       cpassword=request.POST['cpassword']
       
       if password!=cpassword:
           messages.error(request, 'YOUR PASSWORD IS INCORRECT')
           return redirect ("signup")
       if len(password)<=4:
           messages.error(request, "YOUR PASSWORD TOO SHORT,USE MIN 5 CHAR")
           return redirect ("signup")
       UserExist=User.objects.filter(username=username)
       if UserExist:
           messages.error(request, "user name or email already exist....")
           return redirect ("signup")
       add_user=User.objects.create_user(username=username,email=email,password=password)
       request.session['email']=email
       
       #OTP Generate
       otp=str(random.randint(1000 ,9999))
       c = user_otp.objects.create(user = add_user,email=add_user.email, otp=otp)
       receiver=email
       # send mail
       sent(receiver,otp)
       
       return redirect("otp")
    else:
        return render(request,"signup.html")


#Otp verrify
def otp_verify(request):
    
    if request.method=='POST':
        email = request.POST['Email']
        otp=request.POST.get('otp')
        verify_otp = user_otp.objects.get(email=email)
       
        if otp != verify_otp.otp:
           messages.error(request, "Wrong OTP try again") 
           return render(request,"otp.html")
        else:
         return redirect("user_login")     
    return render(request,"otp.html")

#login
def user_login(request):
    if request.method=='POST':
       username=request.POST['username']
       password=request.POST['password']    
       check_user=authenticate(username=username,password=password)
       
       if check_user is not None:
           login(request,check_user)
           request.session['user_id'] = check_user.id
           return redirect('home')
       else:
           return HttpResponse("Invaild username/password")
    else: 
       return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect ("user_login")
