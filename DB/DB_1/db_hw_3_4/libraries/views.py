from django.shortcuts import render, redirect
from .models import Author, Book
from .forms import AuthorForm, BookForm

# Create your views here.
def index(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'libraries/index.html', context)

def detail(request, author_pk):
    author = Author.objects.get(pk=author_pk)
    book_form = BookForm(request.POST)
    books = author.book_set.all()
    context = {
        'author': author,
        'book_form' : book_form,
        'books' : books,
    }
    return render(request, 'libraries/detail.html', context)


def create_book(request, author_pk):
    author = Author.objects.get(pk=author_pk)
    books = author.book_set.all()
    book_form = BookForm(request.POST)
    if book_form.is_valid():
        book = book_form.save(commit=False)
        book.author = author
        book.save()
        return redirect('libraries:detail', author.pk)
    context = {
        'author' : author,
        'books' : books,
        'book_form' : book_form,
    }
    return render(request, 'libraries/detail.html', context)



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
