
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.MyLoginView.as_view(), name="login"),
    path('register/', views.RegisterUserView.as_view(), name='register' ),
    path('logout/', views.MyLogoutView.as_view(), name='logout' ),
    path('lessons/', views.all_lessons, name='lessons' ),
    path('pass_lesson/<int:number>/', views.passed_lesson, name='pass_lesson' ),
    path('lesson/<int:number>/', views.lesson, name='lesson' ),
]
