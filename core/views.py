from django.shortcuts import render

# Create your views here.


class IndexTemplateView(TemplateView):
    template_name = "core/index.html"