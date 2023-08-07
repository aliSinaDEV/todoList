from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages

from django.http import HttpResponse
from . models import Task
from . forms import *


# Create your views here.
def index(request):

    all_tasks = Task.objects.all().order_by('-created')
    form = TaskForm()

    if request.method == 'POST':

        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'all_tasks': all_tasks, 'form':form}
    return render(request, 'tasks/list.html', context)



def delete(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    messages.success(request, 'Task deleted successfully')
    return redirect('/')

def finish(request, id):
    task = get_object_or_404(Task, id=id)
    task.complete = True
    task.save()
    return redirect('/')