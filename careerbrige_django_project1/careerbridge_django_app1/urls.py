from django.urls import path
from . import views
#from careerbridge_django_app1 import views

urlpatterns = [
    #path('',views.home,name='home'),
    path('',views.index,name='index'),
    #path('student_table/', views.students_table,name='student_table')
    path('student_table/',views.student_table,name='student_table')

]
