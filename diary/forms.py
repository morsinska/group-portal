from django import forms
from .models import Grade

class GradeForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        initial=forms.fields.datetime.date.today
    )
    class Meta:
        model = Grade
        fields = ['grade', 'date']
        widgets = {
            'grade': forms.NumberInput(attrs={'min':1, 'max':12})
        }