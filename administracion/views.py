from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView, View
from .forms import Project
from .forms import NewUser
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ProjectModel,IPs
from ipware import get_client_ip
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

class CreateProject(LoginRequiredMixin,FormView):
    model = ProjectModel
    form_class = Project
    template_name = 'register/add_project.html'

    def form_valid(self, form):
        ProjectModel.objects.create(**form.cleaned_data)
        return redirect('index')

class Portafolio_page(View):
    def get(self, request):
        template_name='portafolios/portafolio.html'
        extra_context ={
            'lista': ProjectModel.objects.all()
        }
        ip_user, ip_boolean = get_client_ip(request)
        res = IPs(ip = ip_user)
        res.save()
        return render(request, template_name, extra_context)



class ViewProject(View):
    def get(self, request,id):
        template_name = 'portafolios/projectview.html'
        extra_context ={
            'project': ProjectModel.objects.get(id=id)
        }
        return render(request, template_name, extra_context)
