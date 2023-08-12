from django.urls import path
from task_manager.views import TaskListView,TaskDetailsView,CreateTaskView,TaskDeleteView,TaskUpdateView
urlpatterns = [
    path('',TaskListView.as_view(),name='task_list'),
    path('create/',CreateTaskView.as_view(),name='task_create'),
    path('tasks/<int:pk>',TaskDetailsView.as_view(),name='task_details'),
    path('tasks/<int:pk>/update',TaskUpdateView.as_view(),name='task_update'),
    path('tasks/<int:pk>/delete',TaskDeleteView.as_view(),name='task_delete'),
]
