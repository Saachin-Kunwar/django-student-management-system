from django.contrib import admin
from .models import Student
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','course','created_at')
    search_fields= ('name', 'email','course')
    list_filter=('course','created_at')