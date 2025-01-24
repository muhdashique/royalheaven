from django.urls import path
from . import views  # Ensure this import works correctly

urlpatterns = [
    path('', views.index, name='index'), 
    path('about/',views.about,name='about'),
    path('property/',views.property,name='property'),
    path('contact/',views.contact,name='contact'),
    path('send_email/', views.send_email, name='send_email'),
]