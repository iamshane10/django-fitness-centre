from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, ProfileForm, UserUpdateForm, EmployeeForm, ReviewForm
from .models import Profile, Employee
from django.contrib.auth.models import User
from .decorators import unauthenticated_user
from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.http import HttpResponse
# Create your views here.

@unauthenticated_user
def homePage(request, *args, **kwargs):
    form=ReviewForm(request.POST or None)
    if form.is_valid():
       form.save()
       return redirect('../home')
    context = { 'form':form }
    return render(request, "index.html", context)

@unauthenticated_user
def classesPage(request, *args, **kwargs):
    form=ReviewForm(request.POST or None)
    if form.is_valid():
       form.save()
       return redirect('../home')
    context = { 'form':form }
    return render(request, "classes.html", context)

@unauthenticated_user
def schedulePage(request, *args, **kwargs):
    form=ReviewForm(request.POST or None)
    if form.is_valid():
       form.save()
       return redirect('../home')
    context = { 'form':form }
    return render(request, "schedule.html", context)

@unauthenticated_user
def registerPage(request):
    rForm=RegistrationForm(request.POST or None)
    pForm=ProfileForm(request.POST or None)
    if rForm.is_valid() and pForm.is_valid():
        user = rForm.save()
        profile = pForm.save(commit=False)
        user.profile.phone = pForm.cleaned_data.get('phone')
        user.profile.address = pForm.cleaned_data.get('address')
        user.profile.gender = pForm.cleaned_data.get('gender')
        user.profile.height = pForm.cleaned_data.get('height')
        user.profile.weight = pForm.cleaned_data.get('weight')
        user.profile.goals = pForm.cleaned_data.get('goals')
        user.profile.time = pForm.cleaned_data.get('time')
        user.profile.save()
        return redirect('../login')
    context = {'rForm': rForm,'pForm':pForm}
    return render(request, 'register.html', context)

@unauthenticated_user
def registerEmployee(request):
    rForm=RegistrationForm(request.POST or None)
    pForm=EmployeeForm(request.POST or None)
    if rForm.is_valid() and pForm.is_valid():
        user = rForm.save()
        employee = pForm.save(commit=False)
        user.employee.phone = pForm.cleaned_data.get('phone')
        user.employee.gender = pForm.cleaned_data.get('gender') 
        user.employee.save()
        user.is_staff = True
        user.save()
        group = Group.objects.get(name='staff')
        user.groups.add(group)
        messages.success(request, f'Your account has been created!')
        return redirect('../admin')
    context = {'rForm': rForm,'pForm':pForm}
    return render(request, 'register_employee.html', context)

@login_required
def profileView(request):
    if not request.user.profile.height:
        return redirect('../admin')
    else:
        user1 = request.user.profile
        context = { 'bmi': '%.2f'%(user1.weight/((user1.height/100) * (user1.height/100))) }
        return render(request, 'profile.html', context)

@login_required
def updateView(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileForm(request.POST, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('../profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileForm(instance=request.user.profile)

    context = {
        'rForm': u_form,
        'pForm': p_form
    }

    return render(request, 'update.html', context)

@login_required
def dietView(request):
    user1 = request.user.profile
    if user1.goals == 'Weight Loss':
        template = "Diet Plan WL.html"
    elif user1.goals == "Increase Muscle Mass":
        template = "Diet Plan MG.html"
    else:
        template = "Diet Plan MF.html"
    context = {'bmi':user1.weight/(user1.height * user1.height)}
    return render(request, template, context)

@login_required
def workoutView(request):
    user1 = request.user.profile
    if user1.goals == 'Weight Loss':
        template = "Workout plan WL.html"
    elif user1.goals == "Increase Muscle Mass":
        template = "Workout plan MG.html"
    else:
        template = "Workout plan MF.html"
    context = { }
    return render(request, template, context)