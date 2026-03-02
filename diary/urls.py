from django.urls import path
from .views import StudentListView, SubjectListView, ClassListView, StudentGradeView, MyGradesView

urlpatterns = [
    path("", StudentListView.as_view(), name="student_list"),
    path("subjects/", SubjectListView.as_view(), name="subject_list"),
    path('subjects/<int:subject_id>/classes/', ClassListView.as_view(), name='class_list'),
    path('grades/<int:subject_id>/<int:class_id>/', StudentGradeView.as_view(), name='grades_by_class'),
    path('my-grades/', MyGradesView.as_view(), name='my_grades'),
]