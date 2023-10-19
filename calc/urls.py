from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    # path('add',views.add,name='add'),
    path('bmi',views.bmi,name='bmi'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('products',views.products,name='products'),
]