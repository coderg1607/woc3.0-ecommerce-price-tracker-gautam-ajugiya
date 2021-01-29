from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('amazon',views.amazon,name='services'),
    path('flipkart',views.flipkart,name='services'),
    path('snapdeal',views.snapdeal,name='services'),]