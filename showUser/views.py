from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegistrationForm,EditForm, UserAddressForm
from django.contrib import messages
from django.views import View
from .models import Register
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

class Registration(View):
    def get(self, request):
        userform = RegistrationForm()
        form = UserAddressForm()
        context = {
            'userform':userform,
            'form': form,
        }
        return render(request, 'register.html', context)

    def post(self, request):
        userform = RegistrationForm(request.POST)
        form = UserAddressForm(request.POST)
        if form.is_valid() and userform.is_valid():
            user = userform.save()
            user.save()
            adduser = form.save(commit=False)
            adduser.user = user
            adduser.email = user.email
            form.save()
            messages.success(request, 'Congratulations!! Registered Successfully.')
            return redirect('login')
        context = {
            'userform': userform,
            'form': form,
        }
        return render(request, 'register.html', context)

@login_required(login_url='/accounts/login/')
def userlist(request):
    data = Register.objects.all()
    context = {
            'data': data,
        }
    return render(request, 'home.html', context)

@login_required(login_url='/accounts/login/')
def edituser(request, id):
    if request.method=='GET':
        user = Register.objects.get(id=id)
        userform = EditForm(instance=user)
        form = UserAddressForm(instance=user)
        context = {
            'userform': userform,
            'form': form,
            'user':user,
        }             
        return render(request, 'edit.html', context)  

    else:
        user = Register.objects.get(id=id)
        userform = EditForm(request.POST, instance=user) 
        form = UserAddressForm(request.POST, instance=user)  
        if form.is_valid() and userform.is_valid():
            userform.save()
            form.save()
            return redirect('/') 
    
@login_required(login_url='/accounts/login/')
def deleteuser(request, id):
    data = Register.objects.get(id=id)
    user = User.objects.get(email=data.email) 
    user.delete()
    return redirect('/')

