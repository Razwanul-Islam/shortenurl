from django.shortcuts import render,get_object_or_404,redirect
from .models import shortURL
import uuid

def index(request):
    if request.method=='POST':
        url=request.POST['url']
        newUrl=shortURL.objects.get_or_create(url=url)
        return render(request,'index.html',{'result':True,'shortUrl':newUrl[0]})
    else:
        return render(request,'index.html',{'result':False})

def urlRedirect(request,key):
    url=get_object_or_404(shortURL,key=key)
    return redirect(url.url)
# Create your views here.
