from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

def new(requset):
    return render(requset, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    #1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    #2
    article = Article(title=title, content=content)
    article.save()

    return redirect('articles:detail', article.pk)

def delete(request, pk):
    # 몇번 글 삭제?
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    # 몇번 글 수정? (조회필요)
    article = Article.objects.get(pk=pk)

    title = request.POST.get('title')
    content = request.POST.get('content')

    # article = Article(title=title, content=content)
    article.title = title
    article.content = content
    article.save()

    return redirect('articles:detail', article.pk)

