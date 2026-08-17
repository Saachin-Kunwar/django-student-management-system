from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Student
from .forms import StudentForm
# --- AUTHENTICATION VIEWS ---

def register_view(request):
    if request.user.is_authenticated:
        return redirect('student_list')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('student_list')
    else:
        form = UserCreationForm()
    return render(request, 'students/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('student_list')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('student_list')
    else:
        form = AuthenticationForm()
    return render(request, 'students/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')


# --- STUDENT CRUD VIEWS (PROTECTED) ---

@login_required(login_url='login')
def student_list(request):
    query = request.GET.get('q', '')
    if query:
        students = Student.objects.filter(
            Q(name__icontains=query) | 
            Q(email__icontains=query) | 
            Q(department__name__icontains=query)
        ).select_related('department').prefetch_related('clubs')
    else:
        students = Student.objects.all().select_related('department').prefetch_related('clubs').order_by('-created_at')
    return render(request, 'students/student_list.html', {'students': students, 'query': query})

@login_required(login_url='login')
def student_detail(request, pk):
    student = get_object_or_404(Student.objects.select_related('department').prefetch_related('clubs'), pk=pk)
    return render(request, 'students/student_detail.html', {'student': student})

@login_required(login_url='login')
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully!')
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form, 'title': 'Add New Student'})

@login_required(login_url='login')
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully!')
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form, 'title': 'Edit Student'})

@login_required(login_url='login')
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student deleted successfully!')
        return redirect('student_list')
    return render(request, 'students/student_confirm_delete.html', {'student': student})