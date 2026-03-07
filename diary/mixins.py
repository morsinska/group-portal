from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class TeacherRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class StudentRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return not self.request.user.is_staff