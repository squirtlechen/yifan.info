from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Article
from .form import ArticleForm
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

# Create your views here.
class ArticleListView(ListView):
    queryset = Article.objects.all()
    template_name = 'templates/blog/article_list.html'

class ArticleDetailView(DetailView):
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

class ArticleCreateView(CreateView):
    template_name = 'blog/article_create.html'
    queryset = Article.objects.all()
    form_class = ArticleForm

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ArticleUpdateView(UpdateView):
    template_name = 'blog/article_create.html'
    queryset = Article.objects.all()
    form_class = ArticleForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ArticleDeleteView(DeleteView):
    template_name = 'blog/article_delete.html'
    #queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('blog:Articles')



    
