from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import FormView
from accounts.forms import CastomUserForm


class RegistrationUser(FormView):
    form_class = CastomUserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super(RegistrationUser, self).form_valid(form)
