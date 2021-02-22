from django.shortcuts import render,redirect
from .models import Articles
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from django.utils.text import slugify

# Create your views here.
def showArticles(request):
    ArtiList = Articles.objects.all()
    return render(request,'ArticlesList/AllArticles.html',{'ARTL':ArtiList}) 

def about(request):
    return render(request,'ArticlesList/about.html')


def contact(request):
    return render(request,'ArticlesList/contact.html')  


def article_detail(request,Slg):
    # return HttpResponse(Slg)
   obj = Articles.objects.get(slug=Slg)
   return render(request,'ArticlesList/ArtDetail.html',{'FoundedObj':obj})

@login_required(login_url="/Accounts/login/")
def ArticleCreate(request):
    if request.method=='POST':
        form = forms.createArticle(request.POST,request.FILES)
        if form.is_valid():
            #this to save data to database
            instance = form.save(commit=False)
            instance.author=request.user
            instance.save()
            return redirect('test:Home')
    form = forms.createArticle()
    return render(request,'ArticlesList/NewArticle.html',{'F1':form})
