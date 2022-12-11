from django.shortcuts import render
from django.views.generic import CreateView, FormView, View
from .forms import NewUser

class AdministracionView(View):
    def get(self, request):
            template_name = "administracion/index.html"
            return render(request, template_name)
    


class SignUp(CreateView):
    form = NewUser
    template_name = 'register/registracion.html'

    def form_valid(self, form):
        form.save()
        return redirect('login')

