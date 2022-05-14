from django.urls import path
from .views import ArticleListView, ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView

app_name = 'blog'
urlpatterns = [
    path('<int:id>', ArticleDetailView.as_view(), name='Article'),
    path('', ArticleListView.as_view(), name='Articles'),
    path('create', ArticleCreateView.as_view(), name='Create'),
    path('<int:id>/update', ArticleUpdateView.as_view(), name='article-update'),
    path('<int:id>/delete', ArticleDeleteView.as_view(), name='aritcle-delete'),

]