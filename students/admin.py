from django.contrib import admin
from .models import Student, Department, Club

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code')

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'department', 'created_at')
    search_fields = ('name', 'email', 'department__name')
    list_filter = ('department', 'clubs')