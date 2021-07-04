from django.urls import path
from .views import TaskDelete, TaskDetail, TaskList, TaskCreate, TaskUpdate

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('details/<int:pk>/', TaskDetail.as_view(), name='task-details'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
    path('task/create', TaskCreate.as_view(), name='task-create'),
]
