from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.
# def index(request):
#     return HttpResponse("My To Do App First pages")

def index(request):
    todos = Todo.objects.all()
    # JSON  파일 형태로 데이터가 삽입이 되고, 각각의 데이터는 key, value로 구성되어 있음
    # 여기서 key는 모델에서 만든 content / value는 사용자가 입력한 값이 된다.
    # print(todos)
    # print(todos[0].content)
    content = {'todos': todos}
    return render(request, 'my_to_do_app/index.html', content)

def createTodo(request):
    user_input_str = request.POST['todoContent']
    new_todo = Todo(content = user_input_str)
    new_todo.save()
    return HttpResponseRedirect(reverse('index'))
    # return HttpResponse("Create Todo를 할거야 => " + user_input_str)

def doneTodo(request):
    done_todo_id = request.GET['todoNum']
    print("완료한 todo의 id", done_todo_id)
    todo = Todo.objects.get(id = done_todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse('index'))