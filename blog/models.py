from django.conf import settings
from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    user     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title    = models.CharField(default="",max_length = 60)
    content  = models.TextField(blank=True, null=True)

    def get_article_url(self):
        return reverse("blog:Article", kwargs={"id": self.id})

    def get_absolute_url(self):
        return reverse("blog:Article", kwargs={"id": self.id})