"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import *
from vegi.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', log_in , name='log_in'),

    path('resume/', resume , name='resume'),
    path('about/', about , name='about'),
    path('details/', details , name='details'),
    path('persons/', persons , name='persons'),
    
    path('recipe/', recipe , name='recipe'),

    path('delete_recipe/<id>', delete_recipe , name='delete_recipe'),
    
    path('update_recipe/<id>', update_recipe , name='update_recipe'),

    path('login/', log_in , name='log_in'),#logout_view

    path('logout/', logout_view , name='logout_view') ,

    path('register/', register , name='register'),

    path('marks/<student_id>/', stu_marks , name='stu_marks'),

    path('students/', get_students , name='get_students'),



    path('admin/', admin.site.urls),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)