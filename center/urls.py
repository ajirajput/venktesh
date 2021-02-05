from django.urls import path
from center import views


app_name = "center"

urlpatterns = [
    path('print/<int:pk>/', views.registration_print, name='registration_print'),
    
]
