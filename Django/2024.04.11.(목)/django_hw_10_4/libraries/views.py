from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookListSerializer, BookSerializer
from .models import Book
from rest_framework import status

# Create your views here.


@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def book_detail(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        book = Book.objects.get(pk=book_pk)
        response_data = {'delete' : f"도서 고유 번호 { book.isbn }번의 { book.title }을 삭제하였습니다."}
        book.delete()
        return Response(response_data, status=status.HTTP_204_NO_CONTENT)
