from django.urls import path
from website import views
from .views import index, about, service, gallery, contact

app_name = "website"

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('service/', views.service, name="service"),
    path('gallery/', views.gallery, name="gallery"),
    path('contact/', views.contact, name="contact"),
]
