from django.shortcuts import render, get_object_or_404, redirect
from .models import User_Detail
from .forms import UserForm, Register

# Create your views here.

def profile(request):
    return render(request, 'profile_app/profile.html')

def home(request):
    return render(request, 'profile_app/home.html')

def user_edit(request, pk):
    user = get_object_or_404(User_Detail, pk=pk)
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('profile')
    else:
        form = UserForm(instance=user)
        return render(request, 'profile_app/user_edit.html', {'form': form})

def signUp(request):
    context = {}
    form = Register(request.POST or None)
    if form.is_valid():
        user = form.save()
        form.save()
        return redirect("profile")
    context['form']=form
    return render(request,'registration/sign_up.html',context)
