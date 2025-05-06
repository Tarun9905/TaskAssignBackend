# from django.urls import path
# from .views import UserRegister, UserLogin, TaskView, UserList, UpdateTaskStatusView, TaskByUserNameView
#
# urlpatterns = [
#     path('register/', UserRegister.as_view(), name='user-register'),
#     path('login/', UserLogin.as_view(), name='user-login'),
#     path('users/', UserList.as_view(), name='user-list'),
#     path('tasks/', TaskView.as_view(), name='task-list'),
#     path('task/<int:id>/', TaskView.as_view(), name='task-retrieve-update'),
#     path('task/status/<int:id>/', UpdateTaskStatusView.as_view(), name='task-status-update'),
#     path('tasks/user/<str:name>/', TaskByUserNameView.as_view(), name='tasks-by-username'),
# ]

from django.urls import path
from .views import UserRegister, UserLogin, TaskView, UserList, UpdateTaskStatusView, TaskByUserNameView

urlpatterns = [
    # User-related paths
    path('register/', UserRegister.as_view(), name='user-register'),
    path('login/', UserLogin.as_view(), name='user-login'),
    path('users/', UserList.as_view(), name='user-list'),

    # Task-related paths
    path('tasks/', TaskView.as_view(), name='task-list'),  # GET tasks with filtering
    path('task/<int:id>/', TaskView.as_view(), name='task-retrieve-update'),  # Retrieve or update specific task
    path('task/status/<int:id>/', UpdateTaskStatusView.as_view(), name='update-task-status'),  # Update task status
    path('tasks/<str:name>/', TaskByUserNameView.as_view(), name='tasks-by-user'),  # Get tasks by assigned user name

    # Additional paths if required
    # path('tasks/filter/', TaskFilterView.as_view(), name='task-filter'),  # Optional: separate endpoint for advanced filtering
]
