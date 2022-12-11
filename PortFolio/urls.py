from django.urls import path
from . import views

urlpatterns = [
    path("crear/", views.CreateForm.as_view(), name="crear")
   
]
