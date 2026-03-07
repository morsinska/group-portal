from datetime import date


from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from .models import Student, SchoolClass, Subject, Grade
from .forms import GradeForm
from django.views.generic import CreateView
from django.urls import reverse_lazy



#class RegisterView(CreateView):
#    form_class = RegisterForm
#    template_name = "diary/register.html"
#    success_url = reverse_lazy("login")


class StudentListView(TemplateView):
    template_name = 'diary/student_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        subject_id = self.request.GET.get("subject")

        subjects = Subject.objects.all()
        context["subjects"] = subjects

        grades = Grade.objects.select_related(
            "student", "student__school_class", "subject"
        )

        if subject_id:
            grades = grades.filter(subject_id=subject_id)

        grades = grades.order_by(
            "subject__name",
            "student__school_class__class_number",
            "student__school_class__class_letter",
            "-date"
        )

        context["grades"] = grades
        context["selected_subject"] = subject_id

        return context


class SubjectListView(ListView):
    model = Subject
    template_name = "subject_list.html"
    context_object_name = "subjects"

class ClassListView(ListView):
    template_name = 'diary/class_list.html'
    context_object_name = 'classes'

    def get_queryset(self):
        return SchoolClass.objects.filter(students__isnull=False).distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subject'] = get_object_or_404(Subject, id=self.kwargs['subject_id'])
        return context

class StudentGradeView(TemplateView):
    template_name = 'diary/student_grades.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subject = get_object_or_404(Subject, id=self.kwargs['subject_id'])
        school_class = get_object_or_404(SchoolClass, id=self.kwargs['class_id'])
        students = Student.objects.filter(school_class=school_class)

        context['subject'] = subject
        context['school_class'] = school_class
        context['students'] = students
        context['forms'] = {student.id: GradeForm() for student in students}
        context['today'] = date.today().isoformat()
        return context

    def post(self, request, *args, **kwargs):
        subject = get_object_or_404(Subject, id=kwargs['subject_id'])
        school_class = get_object_or_404(SchoolClass, id=kwargs['class_id'])
        students = Student.objects.filter(school_class=school_class)

        for student in students:
            grade_value = request.POST.get(f'grade_{student.id}')
            grade_date = request.POST.get(f'date_{student.id}')
            if grade_value:
                Grade.objects.create(
                    student=student,
                    subject=subject,
                    grade=int(grade_value),
                    date=grade_date if grade_date else timezone.now().date()
                )
        return redirect(request.path)



class MyGradesView(ListView):
    model = Grade
    template_name = 'diary/my_grades.html'
    context_object_name = 'grades'

    def get_queryset(self):
        return Grade.objects.filter(student__user=self.request.user).select_related('subject', 'student__school_class').order_by('-date')


class GradeUpdateView(UpdateView):
    model = Grade
    form_class = GradeForm
    template_name = 'diary/grade_update.html'
    success_url = reverse_lazy('student_list')






class GradeDeleteView(DeleteView):
    model = Grade
    template_name = 'diary/grade_delete.html'
    success_url = reverse_lazy('student_list')
















#from django.views.generic import ListView
#from .models import Student

#class StudentListView(ListView):
#    model = Student
#    template_name = 'student_list.html'
#    context_object_name = 'students'
#
#    def get_queryset(self):
#        return Student.objects.prefetch_related('grades__subject').all()

