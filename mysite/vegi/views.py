from django.shortcuts import render , redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login
# Create your views here.
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from django.db.models import Q , Sum
from django.shortcuts import get_object_or_404

from django.core import serializers
from django.http import JsonResponse

@login_required(login_url="/login/")
def recipe(request):
    

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
    

    if request.method == 'GET':
        Search_recipe = request.GET.get("Search_recipe")

        if Search_recipe:
            query_all = query_all.filter( recipe_name__icontains =  Search_recipe )

    context = { "recipe" : query_all }
    
  
    return render(request , 'recipe.html' , context )


def delete_recipe(request , id ):

    query_set =receipes.objects.get(id =id )

    query_set.delete()

    return redirect( '/recipe/' )

def update_recipe(request , id ):

    query_set =receipes.objects.get(id =id )

    if request.method == 'POST':
        DATA = request.POST

        recipe_img = request.FILES.get('recipe_image')

        recipe_name = (DATA.get('recipe_name'))
        recipe_desc= (DATA.get('recipe_desc'))

        query_set.recipe_desc = recipe_desc
        query_set.recipe_name = recipe_name

        if recipe_img:
            query_set.recipe_img = recipe_img

        query_set.save()

        return redirect( '/recipe/' )

    context = { "recipe" : query_set }

    return render(request , 'update_recipe.html' , context )



def log_in(request):

    if request.method == 'POST':
        DATA = request.POST

        username = (DATA.get('username'))
        password= (DATA.get('password'))

        if not User.objects.filter( username = username).exists:
             
            messages.error(request, "invalid user , please register")
            return redirect( '/login/' )
        
        user = authenticate( username =  username , password =password )

        if user is None:
            messages.error(request, "invalid credentials ")
            return redirect( '/login/' )
        else:
            login( request, user)

            return redirect( '/recipe/' )
    # For GET requests, render the login form template
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('/login/') 


def register(request):
    if request.method == 'POST':
        DATA = request.POST

        first_name = DATA.get('first_name')
        last_name = DATA.get('last_name')
        email_id = DATA.get('email_id')
        username = DATA.get('Username')
        Password = DATA.get('Password')

        user_check = User.objects.filter(username__iexact=username).exists()

        if user_check:
            messages.error(request, "Username already taken. Please choose a different one.")
            return redirect( '/register/' )

        user = User.objects.create( first_name = first_name , 
                                    last_name = last_name , 
                                    email = email_id ,
                                    username = username   )
        
        user.set_password(Password)
        user.save()

        messages.success(request, "Profile created successfully")


    return render(request , 'register.html'  )




def get_students(request):

    query_set = Student.objects.all()



    if request.GET.get('search'):
        search_text = request.GET.get('search')
        query_set = query_set.filter(
            Q(student_name__icontains = search_text ) |
            #Q(student_address__icontains = search_text ) |
            Q(student_email__icontains = search_text ) |
            Q(student_id__student_id__icontains = search_text ) |
            Q(department__department__icontains = search_text ) 
        )

    paginator = Paginator(query_set, 12)  # Show 25 contacts per page.

    page_number = request.GET.get("page" , 1)
    page_obj = paginator.get_page(page_number)

    context = { "page_obj" : page_obj }

    return render(request , 'report/students.html' , context )



def stu_marks(request ,student_id ):

    #logic for student details
    student_id_object = get_object_or_404(StudentID, student_id=student_id)
    # Fetch student details using the related models
    student_details = Student.objects.filter(student_id=student_id_object).values('student_name', 'student_age', 'department__department', 'student_email', 'student_id__student_id')
    print('---',student_details)
    student_data = ''
    for student_data in student_details:
        student_data = student_data

    #serialized_student_details  = serializers.serialize('json', student_details)

    #logic for rank
    query_set = Subjectmarks.objects.filter( student__student_id__student_id = student_id  )
    # ranks = Student.objects.annotate( marks = Sum( 'studentmarks__marks' ) ).order_by(  '-marks' , '-student_age')#['marks']
    # STU_RANK = -1
    # i=1
    # for rank in ranks:

    #     if student_id == rank.student_id.student_id:
    #         STU_RANK = i
    #         #print("---",STU_RANK)
    #         break
    #     i = i+1

    total_marks = query_set.aggregate(marks=Sum('marks'))['marks'] # or 0

    print(query_set)
    context = { "query_set" : query_set ,  'total_marks' : total_marks ,  'student_data' : student_data 
               
                }

    return render(request , 'report/marks.html' , context )










