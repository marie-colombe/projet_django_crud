from django.urls import path
from . import views

app_name='students'
urlpatterns = [
   path('students/', views.students, name='index'),
   path('adds/', views.add_students_view, name='add'),
   path('edits/<int:id>/', views.edit_students_view, name='edit'),
   path('deletes/<int:id>/', views.delete_students_view, name='delete'),
    
]