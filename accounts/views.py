from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserForm
from .models import User

from django.contrib import messages
# Create your views here.
def registerUser(request):
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            # password hasing using foorm.cleaned_data
            '''password=form.cleaned_data['password']
            user=form.save(commit=False)
            user.role=User.Customer
            user.set_password(password)
            user.save()
            return redirect('registerUser')'''
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
            user.role=User.Customer
            user.save()
            messages.success(request,'User has been registered successfully!!')
            return redirect('registerUser')
    else:
        form=UserForm()
    context={
    'form':form,
    }
    return render(request,'accounts/registerUser.html',context)
