from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdate,ProfileUpdate
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method  == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created! please login to verify')
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {
        'form' : form 
    }
    return render(request, 'users/register.html', context)

@login_required
def profile(request):
    if request.method  == 'POST':
        u_updateForm = UserUpdate(request.POST,instance=request.user)
        p_updateForm = ProfileUpdate(request.POST,request.FILES,
                                        instance=request.user.profile)
        if u_updateForm.is_valid() and p_updateForm.is_valid():
            u_updateForm.save()
            p_updateForm.save()
            messages.success(request, f'Your Profile has been updated')
            return redirect('user-profile')
    else:
        u_updateForm = UserUpdate(instance=request.user)
        p_updateForm = ProfileUpdate(instance=request.user.profile)
    context = {
        'u_updateForm': u_updateForm,
         'p_updateForm': p_updateForm
    }
    return render(request, 'users/profile.html', context)
