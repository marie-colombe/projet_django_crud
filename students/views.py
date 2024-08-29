from django.shortcuts import render,redirect, get_object_or_404
from .forms import StudentsForm
from .models import Students
# Create your views here.

def students(request):
   students = Students.objects.all() 
   return render(request, 'html/students.html',{'students':students})


def add_students_view(request):

 if request.method =='POST':
    add_form = StudentsForm(request.POST)
    if add_form.is_valid():
        print(add_form.cleaned_data)
        add_form.save()
    return redirect('students:index')
 add_form = StudentsForm()
 context = {'add_form':add_form}

 return render(request, 'html/add_students.html',context)






def edit_students_view(request, id):
    
    student = get_object_or_404(Students, id=id)  
    
    if request.method == 'POST':
     if request.POST.get('action') == 'annuler':
      return redirect('students:index')   
        
        
    form = StudentsForm(request.POST, instance=student)  # Pré-remplit le formulaire avec les données existantes
    if form.is_valid():
            form.save()  # Enregistre les modifications dans la base de données
            return redirect('students:index')  # Redirige vers la liste des élèves après la modification
    else:
     form = StudentsForm(instance=student)  # Affiche le formulaire pré-rempli avec les données de l'élève
    
    return render(request, 'html/edit_students.html', {'form': form})

 
   


def delete_students_view(request, id):
    student = get_object_or_404(Students, id=id)  
    student.delete() 
    return redirect('students:index')