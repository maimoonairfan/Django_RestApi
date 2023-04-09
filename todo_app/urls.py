from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListTodoAPIView.as_view(), name='todoApp'),

    # path('todoApp/', views.todoApp, name='todoApp'),
]