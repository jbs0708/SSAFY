from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Book, Review
from .forms import ReviewForm

# Create your views here.
def index(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'libraries/index.html', context)

def detail(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    reviews = book.review_set.all()
    review_form = ReviewForm()
    context = {
        'book': book,
        'reviews' : reviews,
        'review_form' : review_form,
    }
    return render(request, 'libraries/detail.html', context)


@login_required
def create_reviews(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    reviews = book.review_set.all()
    review_form = ReviewForm(request.POST)
    if review_form.is_valid():
        review = review_form.save(commit=False)
        review.book = book
        review.user = request.user
        review.save()
        return redirect('libraries:detail', book.pk)
    context = {
        'review_form' : review_form,
        'book' : book,
        'reviews' : reviews,
    }
    return render(request, 'libraries/detail.html', context)


@require_POST
def delete_reviews(request, book_pk, review_pk):
    review = Review.objects.get(pk=review_pk)
    review.delete()
    return redirect('libraries:detail', book_pk)




# def comments_delete(request, article_pk, comment_pk):
#     comment = Comment.objects.get(pk=comment_pk)
#     comment.delete()
#     return redirect('articles:detail', article_pk)