# from faker import Faker
from django.db.models import Q , Sum
# import random

# from .models import *

# fake = Faker()


# def iteams():

#     for i in range(0 , 10):

#         try:
#             dep_obj =Department.objects.all()
#             dep_index = random.randint(0 ,  len(dep_obj))

#             department = dep_obj[dep_index]
#             student_id = f'STU-0{random.randint(100 , 999)}'

#             student_name = fake.name()
#             student_email = fake.email()
#             student_age = random.randint(15 , 25)
#             student_address = fake.address()

#             student_id_obj = StudentID.objects.create( student_id =student_id )

#             student_obj = Student.objects.create( 
#                 department=    department , 
#                 student_id=    student_id_obj , 
#                 student_name=    student_name , 
#                 student_email=        student_email ,
#                 student_age=    student_age , 
#                 student_address=  student_address


#             )

#         except Exception as e:
#             print("---",e)
       

# #iteams()

# def create_marks():
#     stu_obj = Student.objects.all()

#     for stu in stu_obj:
#         sub_obj = Subject.objects.all()

#         for sub in sub_obj:

#             Subjectmarks.objects.create( student = stu ,  subject =     sub , marks = random.randint(1 , 100)    )


from django.db.models import Count
from .models import *

# # Identify duplicate student_ids and keep one instance of each
# duplicate_ids = StudentID.objects.values('student_id').annotate(count=Count('student_id')).filter(count__gt=1)

# # Loop through duplicate student_ids and keep one instance, delete the rest
# for duplicate in duplicate_ids:
#     student_id = duplicate['student_id']
#     instances = StudentID.objects.filter(student_id=student_id)
#     instances_to_keep = instances.first()
#     instances.exclude(pk=instances_to_keep.pk).delete()



def generate_report_card():
    ranks = Student.objects.annotate( marks = Sum( 'studentmarks__marks' ) ).order_by(  '-marks' , '-student_age')#['marks']
    # STU_RANK = -1
    # i=1
    # for rank in ranks:
    #         Reportcard.objects.create(
    #               student = rank ,
    #               student_rank = i
    #         )
    #         print(rank)
    #         i = i+1
