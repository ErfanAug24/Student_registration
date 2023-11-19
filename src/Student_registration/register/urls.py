from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('create/', views.register_Collegian, name='register_collegian'),
    path('all/', views.view_Collegian, name='view_collegian'),
    path('update/<int:pk>/', views.update_Collegian, name='update-collegian'),
    path('collegian/<int:pk>/delete/', views.delete_Collegian, name='delete-collegian'),
    path('hello', views.hello_word, name="hello-world")
]
