from rest_framework import generics
from .serializer import BlogArticleSerializer
from blog.models import Article

class BlogArticleAPIView(generics.CreateAPIView):
    lookup_field      ='pk'
    serializer_class   = BlogArticleSerializer

    def get_queryset(self):
        return Article.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BlogArticleRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field      ='pk'
    serializer_class   = BlogArticleSerializer

    def get_queryset(self):
        return Article.objects.all()