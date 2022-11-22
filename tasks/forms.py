from django import forms
from .models import Task

class TaskForm(forms.ModelForm): #create Task
    class Meta:   #voy a especificar q modelo pertenece
        model = Task
        fields = ['title', 'description',  'important'] #campos a utilizar en este form
        widgets = {
            'title': forms.TextInput(attrs= { 'class': 'form-control', 'placeholder': 'Write a title'}),
            'description': forms.Textarea(attrs= { 'class': 'form-control', 'placeholder': 'Write a description'}),
            'important': forms.CheckboxInput(attrs= { 'class': 'form-check-input m-auto'}),
            }
        