from django.shortcuts import render

from django.views import View
from django.views.generic import ListView, DetailView

from .models import *


def sample():
    return print(1)


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'main/about.html'
    slug_url_kwarg = 'service_slug'
    context_object_name = 'service'

    def get_context_data(self, *, object_list=None, **kwargs):
        service_slug = self.kwargs.get('service_slug', None)
        price_list = Price.objects.filter(service__slug=service_slug)

        context = super().get_context_data(**kwargs)
        context['title'] = context['service']
        context['price_list'] = price_list
        return context

    # def get(self, request, *args, **kwargs):
    #
    #     if service_slug:
    #         service = Service.objects.get()
    #         print(service[0])
    #         return render(request, 'main/about.html', {"service": service})


class Services(ListView):

    model = Service
    template_name = 'main/index.html'
    context_object_name = 'services'
    allow_empty = False
    # request = sample()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = str(context['services'][0].service_type)
        context['service_type_selected'] = context['services'][0].service_type.pk
        return context

    def get_queryset(self):
        return Service.objects.filter(service_type__slug=self.kwargs['service_type_slug']).prefetch_related()

