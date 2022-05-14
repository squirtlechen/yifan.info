from django.shortcuts import render

# Create your views here.
def home_page(request, *args, **kwargs):
    return render(request, 'index.html', locals())

def styles(request, *args, **kwargs):
    return render(request, 'styles.html', locals())

def force_direct(request, *args, **kwargs):
    return render(request, 'force_direct.html', locals())

def sankey(request, *args, **kwargs):
    return render(request, 'sankey.html', locals())