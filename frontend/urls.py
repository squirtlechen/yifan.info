from django.urls import path
from .views import *

app_name = 'frontend'


urlpatterns = [
    path('', home_page, name='Home'),
    path('styles', styles, name='Style'),
    path('force_direct', force_direct, name='Force'),
    path('sankey', sankey, name='Sankey'),
]
