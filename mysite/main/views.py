from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1> hi i am a django server </h1>')

def resume(request):



    return render(request, 'my_template.html' )

def about(request):



    return render(request, 'about.html' )

def details(request):



    return render(request, 'details.html' )

def persons(request):

    persons = [
    {
        "first_name": "John",
        "last_name": "Doe",
        "age": 30,
        "city": "New York"
    },
    {
        "first_name": "Alice",
        "last_name": "Smith",
        "age": 28,
        "city": "Los Angeles"
    },
    {
        "first_name": "Bob",
        "last_name": "Johnson",
        "age": 35,
        "city": "Chicago"
    },
    {
        "first_name": "Rajesh",
        "last_name": "Kumar",
        "age": 32,
        "city": "Mumbai"
    },
    {
        "first_name": "Priya",
        "last_name": "Sharma",
        "age": 26,
        "city": "Delhi"
    },
    {
        "first_name": "Amit",
        "last_name": "Patel",
        "age": 29,
        "city": "Ahmedabad"
    }
    ]
    
    
    Summary = "Experienced Python Automation Engineer with 2.5 years of hands-on experience in designing and implementing automation solutions for diverse projects. Proficient in Python scripting, automation frameworks, and integration with tools like Splunk and ServiceNow. Expertise in identifying automation opportunities and delivering innovative solutions."


    return render(request, 'persons.html' , context= { 'persons' : persons , 'Summary' : Summary } )