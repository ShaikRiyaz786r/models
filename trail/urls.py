from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage , name='login'),
    path('signup/', views.signup , name='signup'),
    path('add/', views.addEmp , name='add'),
    path('',views.Home , name='home'),
    path('delete/<int:pk>/',views.delete_obj , name='delete'),
    path('update/<int:pk>/',views.update_obj , name='delete'),


]
