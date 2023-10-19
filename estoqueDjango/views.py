from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator
from .models import Products

def index(request):
    produtos = Products.objects.all()
    paginator = Paginator(produtos, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'pages/index.html', {'produtos': produtos})