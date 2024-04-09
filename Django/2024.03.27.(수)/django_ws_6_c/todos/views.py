from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.
def index(request):
    todo_list = Todo.objects.all()
    context = {
        'todo_list': todo_list
    }
    return render(request, 'todos/index.html', context)

# 만든다
def create(request):
    # 입력받은 폼을 가져온다
    form = TodoForm(request.POST)
    # 가져온 방식이 POST인가?
    if request.method == 'POST':
        # 받아온 값이 유효한가?
        if form.is_valid():
            # todo 변수에 입력받은 폼 저장 (pk 추출하려고)
            # => (detail.html 상단의) N(pk)번째 할 일
            todo = form.save()
            return redirect('todos:detail', todo.pk)
    else:
        form = TodoForm()
    context = {
        'form': form
    }
    return render(request, 'todos/create.html', context)

# def new_todo(request):
#     form = TodoForm(request.POST)
#     if form.is_valid():
#         todo = form.save()
#         return redirect('todos:detail', todo.pk)
#     context = {
#         'form': form
#     }
#     return render(request, 'todos/create.html', context)

    
def detail(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    context = {
        'todo': todo
    }
    return render(request, 'todos/detail.html', context)


def delete(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo.delete()
    return redirect('todos:index')

def update(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todos:detail', todo.pk)
    else:
        form = TodoForm(instance=todo)
    context = {
        'todo': todo,
        'form': form
    }
    return render(request, 'todos/update.html', context)

# def edit_todo(request, todo_pk):
#     todo = Todo.objects.get(pk=todo_pk)
#     form = TodoForm(request.POST, instance=todo)
#     if form.is_valid():
#         todo = form.save()
#         return redirect('todos:detail', todo.pk)
#     context = {
#         'todo': todo,
#         'form': form
#     }
#     return render(request, 'todos/update_todo.html', context)