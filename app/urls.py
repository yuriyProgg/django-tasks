from django.urls import path
from app import views

urlpatterns = [
    path("", views.main_view, name="main"),
    path("api/task/<int:pk>/delete", views.task_api_delete, name="delete task"),
    path("api/task/<int:pk>/complete", views.task_api_complete, name="complete task"),
    path("api/tasks", views.tasks_api_view, name="tasks"),
    path("login", views.login_view, name="login"),
    path("registration", views.registration_view, name="registration"),
    path("logout", views.logout_view, name="logout"),
]
