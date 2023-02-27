from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .forms import CustomCreateForms


class CreateUser(generic.CreateView):
    form_class = CustomCreateForms
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')
