from django.views.generic.edit import FormView
from .forms import SignUpForm

class SignUpView(FormView):
    template_name = 'accounts/signup.html'
    form_class = SignUpForm
    success_url = '/home/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
