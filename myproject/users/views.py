from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def register_view(request):
    # If the request method is POST, it means the form has been submitted
    if(request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('posts:list')
    # If the request method is GET, it means the form has not been submitted
    else:
        form = UserCreationForm()
    
    
    return render(request, 'users/register.html', {'form': form})

# login view
def login_view(request):
    if(request.method == 'POST'):
        form = AuthenticationForm(data=request.POST)
        if(form.is_valid()):
            # Login logic
            login(request, form.get_user())
            return redirect('posts:list')
    else:
        form = AuthenticationForm()
    
    return render(request, 'users/login.html', {'form': form})


# logout view
def logout_view(request):
    if(request.method == 'POST'):
        logout(request)
        return redirect('posts:list')
