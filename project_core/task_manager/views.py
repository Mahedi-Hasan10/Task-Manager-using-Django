from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from task_manager.models import Task
from task_manager.forms import TaskForm
from django.shortcuts import render

# Create your views here.
def home(request):
    pass

class TaskListView(ListView):
    model = Task
    template_name = 'task.html'
    context_object_name = 'tasks'
    
class TaskDetailsView(DetailView):
    model = Task
    template_name = 'task_details.html'
    
class CreateTaskView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task_list')
    
class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task_list')
    
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('task_list')
    
