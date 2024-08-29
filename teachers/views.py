from django.shortcuts import render,redirect, get_object_or_404
from .forms import TeachersForm
from .models import  Teachers


# Create your views here.

def teachers(request):
    teachers = Teachers.objects.all()
    return render(request, 'html/teachers.html',{'teachers':teachers})


def add_teachers(request):

    if request.method == 'POST':
    
        prof_form = TeachersForm(request.POST)
  
        if prof_form.is_valid():
            print(prof_form.cleaned_data)
            prof_form.save()
        return redirect('teachers:index')   
    prof_form = TeachersForm()
    context = {'prof_form':prof_form}
    return render(request, 'html/add_teachers.html',context)



def edit_teachers_view(request, id):  

    teacher = get_object_or_404(Teachers, id=id)  
    
    if request.method == 'POST':
     if request.POST.get('action') == 'annuler':
      return redirect('teachers:index')   
       
        
    form = TeachersForm(request.POST, instance=teacher)  
    if form.is_valid():
        form.save()  
        return redirect('teachers:index') 
    else:
     form = TeachersForm(instance=teacher) 
    
    return render(request, 'html/edit_teachers.html', {'form': form})



def delete_teachers_view(request, id):
    teacher = get_object_or_404(Teachers, id=id)  
    teacher.delete() 
    return redirect('teachers:index')