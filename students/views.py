from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Student
from .forms import StudentForm

# 1. READ (List & Search)
def student_list(request):
    query = request.GET.get('q', '')
    if query:
        # Search filter using OR logic (Q objects)
        students = Student.objects.filter(
            Q(name__icontains=query) | 
            Q(email__icontains=query) | 
            Q(course__icontains=query)
        )
    else:
        students = Student.objects.all().order_by('-created_at')
        
    return render(request, 'students/student_list.html', {'students': students, 'query': query})

# 2. READ (Single Record Detail)
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student_detail.html', {'student': student})

# 3. CREATE
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

# 4. UPDATE
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

# 5. DELETE
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student deleted successfully!')
        return redirect('student_list')
    return render(request, 'students/student_confirm_delete.html', {'student': student})