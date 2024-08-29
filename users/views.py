from django.shortcuts import render,redirect, get_object_or_404
from .forms import UsersForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def users_view(request):
    users = User.objects.all() 
    return render(request, 'html/users.html',{'users': users})


def edit_users_view(request, id):  

    context = {
                "title": "modifier utilisateur"
                }
    
    user = get_object_or_404(User, id=id)  
    
    if request.method == 'POST':
     if request.POST.get('action') == 'annuler':
      return redirect('users:index')   
       
        
    form = UsersForm(request.POST, instance=user)  
    if form.is_valid():
        form.save()  
        return redirect('users:index') 
    else:
     form = UsersForm(instance=user) 
     context["form"] = form
    
    return render(request, 'html/edit_users.html', context)



def add_users_view(request):
     
     if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        if not username or not password:
           return render(request,'html/add_users.html')
        else:
           user = User(username= username)
           user.save()
           user.password = password
           user.set_password(user.password)
           user.save()
           return redirect('users:index')
     return render(request,'html/add_users.html')
        
     
     
    
   