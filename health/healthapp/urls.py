from django.urls import path
from healthapp import views

urlpatterns = [
    path('contact/', views.contact,name='contact'),
    path('login/', views.login,name='login'),
    path('logout/', views.logout,name='logout'),
    path('register/', views.register,name='register'),
    path('bmi/', views.bmi,name='bmi'),
]
