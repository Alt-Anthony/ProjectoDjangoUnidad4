from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView, View
from .forms import Project
from .forms import NewUser
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ProjectModel

class AdministracionView(View):
    def get(self, request):
            template_name = "administracion/index.html"
            return render(request, template_name)
    


class SignUp(CreateView):
    form_class = NewUser
    template_name = 'register/registracion.html'

    def form_valid(self, form):
        form.save()
        return redirect('login')

class CreateProject(FormView):
    model = ProjectModel
    form_class = Project
    template_name = 'register/add_project.html'

    def form_valid(self, form):
        ProjectModel.objects.create(**form.cleaned_data)
        return redirect('main')

class Portafolio_page(View):
    def get(self, request):
        template_name='portafolios/portafolio.html'
        extra_context ={
            'lista': ProjectModel.objects.all()
        }

        return render(request, template_name, extra_context)