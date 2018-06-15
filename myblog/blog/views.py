from django.shortcuts import render
from django.http import  HttpResponse
from . import models
# Create your views here.
def index(request):
#    article = models.Article.objects.get(pk=2)
    article = models.Article.objects.all()
    return render(request,'blog/index.html',{'article':article})
def article_page(request,article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request,'blog/article_page.html',{'article':article})
def article_edit(request,article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request,'blog/edit_page.html',{'article':article})
def edit_action(request,article_id):
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    attr = models.Article.objects.get(pk=article_id)
    attr.title = title
    attr.content = content
    attr.save()
    return render(request,'blog/article_page.html',{'article':attr})
def add_page(request):
    return render(request, 'blog/add_page.html')
def create_page(request):
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    models.Article.objects.create(title=title, content=content)
    article = models.Article.objects.all()
    return render(request, 'blog/index.html', {'article': article})