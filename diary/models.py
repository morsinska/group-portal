from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предмети"
        ordering = ['name']

    def __str__(self):
        return self.name


class SchoolClass(models.Model):
    class_number = models.IntegerField()
    class_letter = models.CharField(max_length=1)

    class Meta:
        verbose_name = "Клас"
        verbose_name_plural = "Класи"
        ordering = ['class_number', 'class_letter']
        unique_together = ('class_number', 'class_letter')

    def __str__(self):
        return f"{self.class_number}-{self.class_letter}"



class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE, related_name="students")

    class Meta:
        verbose_name = "Учень"
        verbose_name_plural = "Учні"

    def __str__(self):
        return f"{self.user.username} ({self.school_class})"


class Grade(models.Model):
    GRADES_CHOICES = [(i, str(i)) for i in range(1, 13)]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.IntegerField(choices=GRADES_CHOICES)
    date = models.DateField()

    class Meta:
        verbose_name = "Оцінка"
        verbose_name_plural = ("Оцінки")
        ordering = ['-date']

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.grade}"

















