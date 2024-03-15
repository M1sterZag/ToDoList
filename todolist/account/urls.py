from django.urls import path, include
from . import views

urlpatterns = [
    # post views
    path('', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout-then-login/', views.logout_then_login, name='logout_then_login'),
    path('tasks/', include('tasks.urls')),
]
