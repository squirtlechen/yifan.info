from django.conf.urls import url
from .view import BlogArticleRudView,BlogArticleAPIView

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', BlogArticleRudView.as_view(), name='post-rud'),
    url(r'^$', BlogArticleAPIView.as_view(), name='post-creat'),
]