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
    