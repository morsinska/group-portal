from django.urls import path
from .views import StudentListView, SubjectListView, ClassListView, StudentGradeView, MyGradesView, GradeUpdateView, GradeDeleteView



urlpatterns = [
    path("", StudentListView.as_view(), name="student_list"),
    path("subjects/", SubjectListView.as_view(), name="subject_list"),
    path('subjects/<int:subject_id>/classes/', ClassListView.as_view(), name='class_list'),
    path('grades/<int:subject_id>/<int:class_id>/', StudentGradeView.as_view(), name='grades_by_class'),
    path('my-grades/', MyGradesView.as_view(), name='my_grades'),
    path("grade/<int:pk>/edit/", GradeUpdateView.as_view(), name="grade_edit"),
    path("grade/<int:pk>/delete/", GradeDeleteView.as_view(), name="grade_delete"),
]