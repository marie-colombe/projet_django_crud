from django.urls import path

from . import views

app_name='users'

urlpatterns = [
   path('users/', views.users_view, name='index'),
    path('addu/', views.add_users_view, name='add'),
    path('editu/<int:id>/', views.edit_users_view, name='edit'),
    
]

