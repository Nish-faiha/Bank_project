from django.urls import path
from . import views
urlpatterns=[
    path('',views.base,name='base'),
    path('register', views.register, name='register'),
    path('login',views.login,name='login'),
    path('newpage',views.newpage,name='newpage'),
    path('customer',views.customer,name='customer'),
    path('submit',views.submit,name='submit'),
    path('logout',views.logout,name='logout'),
]
