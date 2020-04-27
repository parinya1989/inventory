from django.shortcuts import render
from .models import Product
# from django.http import HttpResponse

# Create your views here.
def index(request):
    product = Product.object.all()
    # html="<html><body>Home page</body></html>"
    # return HttpResponse(html)
    return render(request, 'frontend/index.html',{'product':product})

def index(request):
    return render(request, 'frontend/about.html')

def index(request):
    return render(request, 'frontend/contact.html')