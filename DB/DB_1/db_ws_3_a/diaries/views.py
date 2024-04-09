from django.shortcuts import render, redirect
from .models import Diary
from .forms import DiaryForm

# Create your views here.
def index(request):
    diaries = Diary.objects.all()
    context = {
        'diaries': diaries,
    }
    return render(request, 'diaries/index.html', context)

def create(request):
    if request.method == 'POST':
        form = DiaryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('diaries:index')
    else:
        form = DiaryForm()
    context = {
        'form': form
    }
    return render(request, 'diaries/create.html', context)


def comment_create(request, diary_pk):
    diary = Diary.objects.get(pk=diary_pk)
    



# def comments_create(request, pk):
#     article = Article.objects.get(pk=pk)
#     comments = article.comment_set.all()
#     comment_form = CommentForm(request.POST)
#     if comment_form.is_valid():
#         comment = comment_form.save(commit=False)
#         comment.article = article
#         comment.save()
#         return redirect('articles:detail', article.pk)
#     context = {
#         'article' : article,
#         'comment_form' : comment_form,
#         'comments' : comments,
#     }
#     return render(request, 'articles/detail.html', context)