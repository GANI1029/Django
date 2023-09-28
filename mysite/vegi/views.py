from django.shortcuts import render , redirect
from .models import *


# Create your views here.


def recipe(request):
    

    # for i in receipes.objects.all():
    #     i.delete()

    if request.method == 'POST':
        DATA = request.POST
        recipe_img = request.FILES.get('recipe_image')

        print(DATA.get('recipe_name'))
        print(DATA.get('recipe_desc'))
        print(recipe_img)
        recipe_name = DATA.get('recipe_name')

        if recipe_name is not None and recipe_name.strip(): 
            receipes.objects.create(  recipe_name = recipe_name  , recipe_desc = DATA.get('recipe_desc') , recipe_image = recipe_img )

        return redirect( '/recipe/' )
        
    query_all =receipes.objects.all()

    context = { "recipe" : query_all }
    
  
    return render(request , 'recipe.html' , context )


def delete_recipe(request , id ):

    query_set =receipes.objects.get(id =id )

    query_set.delete()

    return redirect( '/recipe/' )
