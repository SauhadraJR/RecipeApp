from django.shortcuts import render, redirect
from .models import Recipe

# Create your views here.

def home(request):
    recipe_obj = Recipe.objects.all()
    data = {'recipes':recipe_obj}
    return render(request,'index.html',context = data)

def create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        category = request.POST.get("category")
        process = request.POST.get("process")
        ingredients = request.POST.get("ingredients")
        picture = request.FILES.get("picture")
        Recipe.objects.create(picture = picture, name= name ,description= description , category = category, process = process, ingredients = ingredients)
        return redirect("home")
    return render(request, 'create.html')

def edit(request,pk):
    Recipe_obj = Recipe.objects.get(id=pk)
    data = {'Recipe':Recipe_obj}
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        category = request.POST.get("category")
        process = request.POST.get("process")
        ingredients = request.POST.get("ingredients")
        picture = request.POST.get("picture")
        
        Recipe_obj.name = name
        Recipe_obj.description = description
        Recipe_obj.category = category
        Recipe_obj.process = process
        Recipe_obj.ingredients = ingredients
        Recipe_obj.picture = picture

        Recipe_obj.save()
        return redirect("home")
    return render(request, 'edit.html',context = data)
    

def delete(request,pk):
    Recipe_obj = Recipe.objects.get(id=pk)
    data = {'Recipe':Recipe_obj}
    if request.method == "POST":
        Recipe_obj.delete()
        return redirect("home")

    return render(request, 'delete.html',context = data)

def deleteall(request):
    Recipe_objects = Recipe.objects.all()
    if request.method == "POST":
        Recipe_objects.delete()
        return redirect('home')
    return render(request, 'deleteall.html')

