from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout

# Create your views here.
def SignUp_view(request):
    
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('test:Home')
        else:
            return render(request,'Accounts/SignUpForm.html',{'Form':form})
    else:
        form=UserCreationForm()
        return render(request,'Accounts/SignUpForm.html',{'Form':form})

def login_view(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                
                return redirect('test:Home')
        else:
            return render(request,'Accounts/loginForm.html',{'Form':form})  
    else:
        form=AuthenticationForm()
        return render(request,'Accounts/loginForm.html',{'Form':form})  


def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('test:Home')



