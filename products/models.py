from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title       = models.CharField(default="This is title",max_length = 60)
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=10000)
    summary     = models.TextField(blank=True, null=False)

    def get_product_url(self):
        return reverse("products:Product", kwargs={"id": self.id}) #f"/products/{self.id}"
