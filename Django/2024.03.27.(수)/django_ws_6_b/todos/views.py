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

def create_todo(request):
    form = TodoForm()
    context = {
        'form' : form,
    }
    # print(form)
    return render(request, 'todos/create_todo.html', context)

def detail(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    context = {
        'todo': todo
    }
    return render(request, 'todos/detail.html', context)

def new_todo(request):
    form = TodoForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            todo = form.save()
            return redirect('todos:detail', todo.pk)
    else:
        form = TodoForm()
    context = {
        'form' : form,
    }
    # work = request.POST.get('work')
    # content = request.POST.get('content')
    # is_completed = False

    # todo = Todo(work=work, content=content, is_completed=is_completed)
    # todo.save()
    return render(request, 'todos/create_todo.html', context)

def delete_todo(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo.delete()
    return redirect('todos:index')

def update_todo(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todos:detail', todo.pk)
    else:
        form = TodoForm(instance=todo)
    # todo = Todo.objects.get(pk=todo_pk)
    context = {
        'form' : form,
        'todo': todo,
    }
    return render(request, 'todos/update_todo.html', context)

# def edit_todo(request, todo_pk):
#     todo = Todo.objects.get(pk=todo_pk)
#     form = TodoForm(request.POST)
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect('todos:detail.html', todo.pk)
#     else:
#         form = TodoForm()
#     context = {
#         'todo' : todo
#     }

    # work = request.POST.get('work')
    # content = request.POST.get('content')

    # todo.work = work
    # todo.content = content
    # todo.save()
    # return render(request, 'todos:detail.html', todo.pk, context)