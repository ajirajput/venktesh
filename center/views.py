from django.shortcuts import render
from .models import RegistrationDetails

# Create your views here.
def registration_print(request, pk):
    objdata = RegistrationDetails.objects.filter(pk=pk)
    return render(request, 'website/print.html', {'data':objdata})
