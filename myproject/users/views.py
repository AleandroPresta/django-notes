from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register_view(request):
    # If the request method is POST, it means the form has been submitted
    if(request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:list')
    # If the request method is GET, it means the form has not been submitted
    else:
        form = UserCreationForm()
    
    
    return render(request, 'users/register.html', {'form': form})


