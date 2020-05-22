from django.contrib.auth.mixins import LoginRequiredMixin
from django.apps import apps
from django.views.generic import DetailView, CreateView
from django.http import HttpResponse, HttpRequest, request
from django.core.signals import request_finished
from django.dispatch import receiver

Company = apps.get_model('Company', 'Company')


class PostDetailView(DetailView):
    model = Company

    def get_object(self, *args, **kwargs):
        obj = super().get_object()
        try:
            self.request.session['viewed']
        except KeyError:
            self.request.session['viewed'] = False
        else:
            pass
        while not self.request.session['viewed']:
            obj.total_viewers += 1
            obj.save()
            self.request.session['viewed'] = True
            return obj
        return obj


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Company
    fields = ['name', 'logo', 'address']
