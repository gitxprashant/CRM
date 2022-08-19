from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from gst import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode 
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from . models import CustomUser
import datetime

# Create your views here.

def home(request):    

    return render(request,"authentication/index.html")

def signup(request, **kwargs):
    
    if request.method == "POST":
        
        username=request.POST['username']
        email=request.POST['email']
        number=request.POST['number']
        pwd=request.POST['pwd']
        pwd1=request.POST['pwd1']

        if CustomUser.objects.filter(username=username):

            messages.error(request, "Username Already Exist! Please try another Username.")

            return redirect("home")

        if CustomUser.objects.filter(email=email):

            messages.error(request, "Email Already Registered! Please try another Email.")

            return redirect("home")

        if pwd != pwd1:

            messages.error(request, "Password didn't matched. Please try again.")

            return redirect("home")

        myuser=CustomUser.objects.create_user(username, email, pwd)

        myuser.number = number

        myuser.is_active = False

        myuser.save()

    #SIGNUP EMAIL:

        subject='WELCOME TO GST SERVICE CENTER'

        message="Hello " + myuser.username + "!!\n" + "Welcome to GST SERVICE CENTER"

        from_email= settings.EMAIL_HOST_USER

        to_list=[myuser.email]

        send_mail(subject, message, from_email, to_list, fail_silently=False)

    #CONFIRMATION EMAIL:

        current_site=get_current_site(request)

        email_subject= "Confirm Your EMAIL @ GST SERVICE CENTER"

        message2=render_to_string("email_confirmation.html",{ 
            'name': myuser.username,
            'domain': current_site.domain,
            'uid' : urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': default_token_generator.make_token(myuser),
        })

        email=EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email]
            )
        email.fail_silently=False
        email.send()

        return redirect('signin')
        
    return render(request,"authentication/signup.html")
    
def signin(request):

    if request.method == "POST":

        username=request.POST['username']

        pwd=request.POST['pwd']

        user = authenticate(username=username,password=pwd)

        if user is not None and user.is_active:

            login(request,user)

            username=user.username

            return render(request,"authentication/index.html",{'username':username})

        else:

            messages.error(request,"Bad Credentials!")

            return redirect('home')            

    return render(request,"authentication/signin.html")

def signout(request):

    request.user.last_logout = datetime.datetime.now()
    
    request.user.save()

    logout(request)

    messages.success(request,"You Are Successfully Logged Out.")

    return redirect("home")

def activate(request, uidb64, token):
    try:

        uid=force_str(urlsafe_base64_decode(uidb64))

        myuser=CustomUser.objects.get(pk=uid)
    
    except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        
        myuser= None

    if myuser is not None and default_token_generator.check_token(myuser, token):

        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        return redirect("home")

    else:

        return redirect(request, 'activation_failed.html')

















