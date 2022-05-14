from django.urls import path
from .views import *


app_name = 'analysis'
urlpatterns = [
     path('test', test_plotly, name='test')
]

