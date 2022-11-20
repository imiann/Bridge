from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Plan

class Planlist(ListView):
    model = Plan
    context_object_name = 'plans'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = context['plans'].filter(complete=False).count()


        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['plans'] = context['plans'].filter(title__startswith=search_input)

        context['search_input'] = search_input

        return context






class Plandetail(DetailView):
    model = Plan
    context_object_name = 'plan'
    template_name = 'base/plan.html'

class Plancreate(CreateView):
    model = Plan
    fields = '__all__'
    success_url = reverse_lazy('plans')

class Planupdate(UpdateView):
    model = Plan
    fields = '__all__'
    success_url = reverse_lazy('plans')


class DeleteView(DeleteView):
    model = Plan
    context_object_name = 'plan'
    success_url = reverse_lazy('plans')