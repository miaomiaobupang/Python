from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'myblog/index.html',{'title':'啊啊啊啊啊'})