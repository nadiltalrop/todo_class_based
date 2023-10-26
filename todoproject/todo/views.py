from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from todo.frorms import TaskForm

from.models import Task

# class basedinte imports 
from django.views.generic import ListView, DetailView,UpdateView,DeleteView



# class based 
class TaskListView(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'tasks'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('todo:cvdetails', kwargs={'pk': self.object.id})


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('todo:home')


# function based 

def home(request):
     
    tasks = Task.objects.all()
    print(tasks)

   
    if request.method == 'POST':
        name = request.POST.get('task')
        priority = request.POST.get('priority')
        date = request.POST.get('date')

        tasks = Task.objects.create(name=name, priority=priority,date=date)
        tasks.save()
        return redirect('todo:home')
    
    context = {
        'tasks': tasks
    }

    return render(request, 'home.html',context=context)


def delete(request, id):

    if request.method == 'POST':
        if Task.objects.filter(id=id).exists():
            task = Task.objects.get(id=id)
            task.delete()
            return redirect('todo:home')
        else:
            pass
    
    return render(request,'delete.html')


def update(request, id):
    task = Task.objects.get(id=id)
    form = TaskForm(request.POST or None, instance=task)

    if form.is_valid():
        form.save()
        return redirect('todo:home')
    
    context = {
        'form': form
    }

    return render(request, 'update.html', context=context)
    
