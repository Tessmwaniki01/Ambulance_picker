from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('public_register/', views.public_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('admin/', views.admin, name='admin'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('update_profile/', views.update_profile, name='update'),
    path('owner_home/', views.owners, name='owner_home'),
    path('add_ambulance/', views.add_ambulance, name='add_ambulance'),
    path('ambulance/<int:ambulance_id>/', views.single_ambulance, name='single_ambulance'),
    path('update/<int:ambulance_id>/details', views.update_ambulance, name='update_ambulance'),
    path('delete/<int:ambulance_id>/', views.delete_ambulance, name='delete_ambulance'),
    path('services/', views.services, name='services'),
    path('user_ambulance/<int:ambulance_id>/', views.user_single_ambulance, name='user_single_ambulance'),
    path('comment/<int:ambulance_id>/', views.comment, name='comment'),
    path('hire/<int:ambulance_id>/', views.order, name='order'),
    
    
]
