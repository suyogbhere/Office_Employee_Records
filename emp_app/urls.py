from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('all_emp',views.all_emp_page,name='all_emp'),
    path('add_emp',views.add_emp_page,name='add_emp'),
    path('remove_emp',views.remove_emp_page,name='remove_emp'),
    path('remove_emp/<int:emp_id>',views.remove_emp_page,name='remove_emp'),
    path('filter_emp',views.filter_emp_page,name='filter_emp'),
]
