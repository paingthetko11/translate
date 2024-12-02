from django.shortcuts import render
from .models import *

# Create your views here.
from django.utils.translation import get_language#translate

def Category_List(request):
    category =  Category.objects.all().order_by('-id')
    context  = {
        'category': category,
        'LANGUAGE_CODE' : get_language(),
        }
    #'language_code'
    return render(request, 'index.html', context)


