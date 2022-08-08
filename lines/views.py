from django.shortcuts import render

# some_app/views.py
from django.views.generic import TemplateView


class AppView(TemplateView):
    template_name = "calc.html"


class HomeView(TemplateView):
    template_name = "base.html"
