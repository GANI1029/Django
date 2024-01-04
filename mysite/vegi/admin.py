from django.contrib import admin
from . models import *

admin.site.register(receipes)
admin.site.register(Department)
admin.site.register(StudentID)
admin.site.register(Student)
from django.db.models import Q , Sum
admin.site.register(Subject  )

##gani 1234

class subjectmarksview(admin.ModelAdmin):
    list_display = [ 'student' , 'subject' , 'marks' ]


admin.site.register(Subjectmarks , subjectmarksview )

# Register your models here.

class Reportcardadmin(admin.ModelAdmin):
    list_display = [ 'student' , 'student_rank' , 'total_marks' , 'date_of_report_cardcreation']
    ordering = ['student_rank']

    def total_marks(self , obj):
        student_marks = Subjectmarks.objects.filter(student = obj.student)

        marks = student_marks.aggregate( marks = Sum('marks') )#['marks']
        
        return (marks['marks'])


admin.site.register(Reportcard , Reportcardadmin )