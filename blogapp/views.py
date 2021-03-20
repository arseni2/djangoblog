from django.utils import timezone
from django.views.generic.detail import DetailView
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from blogapp.models import Arcticle

from blogapp.form import CustomUserCreationForm


class ArticleListView(ListView):
    template_name = 'blogapp/html/index.html'
    model = Arcticle
    context_object_name = 'object'
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['textTest'] = 'TESTISUPPERCASE'
        return context

class ArticleDetailView(DetailView):
    template_name = 'blogapp/html/detail.html'
    model = Arcticle

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class CreateArticle(CreateView):
    model = Arcticle
    fields = ['title','body']
    success_url = reverse_lazy('home')
    template_name_suffix = '_create_article'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'blogapp/html/signup.html'
