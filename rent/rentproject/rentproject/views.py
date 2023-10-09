from django.shortcuts import render, redirect
from store_app.models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def base(request):
    return render(request,'Main/base.html')

def about_us(request):
    return render(request,'Main/about_us.html')

def service(request):
    return render(request,'Main/service.html')

def contact(request):
    if request.method == 'POST':
        # Process the form data
        name = request.POST.get('name', )
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Create and save a Contact instance
        contact = Contact(
            name=name,
            email=email,
            phone=phone,
            message=message,
        )
        contact.save()
        return redirect('base')

    return render(request, 'Main/contact.html')

def furniture(request):
    return render(request,'Main/furniture.html')

def appliances(request):
    return render(request,'Main/appliances.html')

def gatgets(request):
    return render(request,'Main/gatgets.html')

def decoration(request):
    return render(request,'Main/decoration.html')




def Handlesignup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        customer = User.objects.create_user(username=username, email=email, password=pass1)
        customer.first_name = first_name
        customer.last_name = last_name
        customer.save()

        return redirect('base')


    return render(request, 'Main/Registration/auth.html')


def Handlesignin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect('base')
        else:
            return redirect('signin')


    return render(request, 'Main/Registration/auth.html')


def enquiry(request):
    return render(request,'Main/enquiry.html')