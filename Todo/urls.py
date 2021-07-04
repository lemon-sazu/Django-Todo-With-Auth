from django.urls import path
from .views import CustomLoginView, RegistrationPage, TaskDelete, TaskDetail, TaskList, TaskCreate, TaskUpdate
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('registration/', RegistrationPage.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', TaskList.as_view(), name='tasks'),
    path('details/<int:pk>/', TaskDetail.as_view(), name='task-details'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
    path('task/create', TaskCreate.as_view(), name='task-create'),
]
