from django.contrib import admin
from .models import Task


# para poder ver en el panel los readonly
class TaskAdmin(admin.ModelAdmin): 
    readonly_fields = ('created', ) #es una tupla


# Register your models here.

admin.site.register(Task, TaskAdmin)
