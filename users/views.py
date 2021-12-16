from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form. cleaned_data.get['username']
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form=UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

@login_requred
def profile(request):
    return render(request, 'user/profile.html')