from django.shortcuts import render
from .models import Recipe

# Create your views here.

def home(request):
    recipe_obj = Recipe.objects.all()
    data = {'recipes':recipe_obj}
    return render(request,'index.html',context = data)

