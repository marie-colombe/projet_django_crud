from django.urls import path
from . import views

app_name='teachers'
urlpatterns = [
    path('teachers/', views.teachers, name='index'),
    path('addt/', views.add_teachers , name='add'),
    path('editt/<int:id>/', views.edit_teachers_view, name='edit'),
    path('deletet/<int:id>/', views.delete_teachers_view, name='delete'),
    
]