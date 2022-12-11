from django.urls import path
from . import views

urlpatterns = [
    path("",views.AdministracionView.as_view(), name="index"),
    path('register/', views.SignUp.as_view(), name='register'),

]
