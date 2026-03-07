from django import forms
from .models import Grade, Student, SchoolClass


#class RegisterForm(forms.ModelForm):

#    password = forms.CharField(widget=forms.PasswordInput)
#    school_class = forms.ModelChoiceField(
#        queryset=SchoolClass.objects.all(),
#        required=False
#    )

#    class Meta:
#        model = User
#        fields = ["username", "password"]

#    def save(self, commit=True):
#        user = super().save(commit=False)
#        user.set_password(self.cleaned_data["password"])

#        if commit:
#            user.save()
#
#            school_class = self.cleaned_data.get("school_class")
#
#            if school_class:
#                Student.objects.create(
#                    user=user,
#                    school_class=school_class
#                )

#        return user



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