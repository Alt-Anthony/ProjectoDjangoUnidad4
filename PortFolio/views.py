from django.shortcuts import render
from django.views import View
from .forms import WebForm 

class CreateForm(View):
    def get(self, request):
        context= { 'form': WebForm}
        return render(request, 'form.html', context)

    def post(self, request):
        pass

