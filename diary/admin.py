from django.contrib import admin
from .models import Student, Subject, Grade, SchoolClass

admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Grade)
admin.site.register(SchoolClass)