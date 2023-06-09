from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserForm
from .models import User,UserProfile
from vendor.forms import VendorForm


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
            print("invalide form")
    else:
        form=UserForm()
    context={
    'form':form,
    }
    return render(request,'accounts/registerUser.html',context)




def registerVendor(request):
    if request.method=='POST':
        form=UserForm(request.POST)
        v_form=VendorForm(request.POST,request.FILES)
        if form.is_valid() and v_form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            username=form.cleaned_data['username']
            user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
            user.role=User.vendor
            user.save()
            vendor=v_form.save(commit=False)
            vendor.user=user
            user_profile=UserProfile.objects.get(user=user)
            vendor.user_profile=user_profile
            vendor.save()
            messages.success(request,'Registored successfully. Please wait for approval !!')
            return redirect('registerVendor')
        else:
            print("invalide form")
            print(form.errors)
    else:
        v_form=VendorForm()
        form=UserForm()
    context={
    'form':form,
    'v_form':v_form,
    }
    return render(request,'accounts/registerVendor.html',context)
