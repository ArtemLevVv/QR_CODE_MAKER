from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .forms import User_Form, Login_Form
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def render_reg(request: HttpRequest):
    form = User_Form()
    if request.method == "POST":
        form_post = User_Form(request.POST, request.FILES)
        if form_post.is_valid():
            username = form_post.cleaned_data.get('username')
            email = form_post.cleaned_data.get('email')
            password = form_post.cleaned_data.get('password')
            second_password = form_post.cleaned_data.get('second_password')
            print(username, email, password, second_password )

        if password != second_password:
            return HttpResponse("Паролі не співпадають", status=400)
        if User.objects.filter(username=username).exists():
            return HttpResponse("Цей username вже зайнятий", status=400)
        if User.objects.filter(email=email).exists():
            return HttpResponse("Цей email вже зареєстровано", status=400)
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        return redirect('login')

    return render(
        request = request,
        template_name= 'reg/reg.html',
        context={
            "form":form,
        },
    )

def render_log(request:HttpRequest):
    form = Login_Form()
    if request.method == "POST":
        form_post = Login_Form(request.POST, request.FILES)
        if form_post.is_valid():
            username  = form_post.cleaned_data.get('username')
            password = form_post.cleaned_data.get('password')
            print(username, password)

            user = authenticate(request=request, username= username, password= password)

            print(user)

            if user is not None:
                login(request= request, user= user)
                return redirect('home')
            else:
                return render(
                    request = request,
                    template_name= 'log/log.html',
                        context={
                        "form":form,
                    },
                )

    return render(
        request = request,
        template_name= 'log/log.html',
            context={
            "form":form,
        },
    )

def render_logout(request:HttpRequest):
    logout(request)
    return redirect('home')  
