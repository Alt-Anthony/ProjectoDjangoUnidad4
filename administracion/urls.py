from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, logout_then_login

urlpatterns = [
    path("",views.AdministracionView.as_view(), name="index"),
    path('registracion/', views.SignUp.as_view(), name='registro'),
    path('project/', views.CreateProject.as_view(), name='create_project'),
    path('login/', LoginView.as_view(), name='login'),
    path('portafolios', views.Portafolio_page.as_view(), name='portafolios')
]
