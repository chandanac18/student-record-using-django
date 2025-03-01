from django import forms
from studentsrecord.models import Student

class StudentForm(forms.ModelForm): 
    class Meta:
        model = Student
        fields = ['name', 'usn', 'course']  
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}) 
        }
