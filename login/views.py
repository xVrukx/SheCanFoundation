from django.shortcuts import render,redirect

from login.models import *

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        number = request.POST['number']

        new_user = Register.objects.create(
            username=username,
            email=email,
            password=password, 
            number=number
        )

        request.session['new_user'] = new_user.id
        print("User ID stored in session:", new_user.id)  #

        return redirect('dashboard:dashboard')
    return render(request, 'login_.html')

