from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model =Product
        fields = [
            'title',
            'description',
            'price',
            'summary'
        ]

class RawProductForm(forms.Form):
    title       = forms.CharField(label='Title')
    description = forms.CharField(
                        required=False,
                        widget=forms.Textarea(
                            attrs={
                                "class":"some class name",
                                "rows":1,
                                "columns":40
                            }
                          )
                        )                        
    price       = forms.DecimalField()