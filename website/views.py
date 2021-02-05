from django.shortcuts import render
from .models import Service, Gallery, contact
from .forms import ContactForm
# Create your views here.


def index(request):
    try:
        __context = {}
        objService = Service.objects.filter(
            is_active=True).order_by('-pk')[0:5]

        objGallery = Gallery.objects.filter(
            is_active=True).order_by('-pk')[0:5]

        __context['MainServices'] = objService
        __context['MainGallery'] = objGallery
        return render(request, 'website/index.html', __context)
    except Exception as ex:
        return render(request, 'website/404.html', {'err': ex})


def about(request):
    try:
        __context = {}
        objService = Service.objects.filter(
            is_active=True).order_by('-pk')

        __context['MainServices'] = objService
        return render(request, 'website/about.html', __context)
    except Exception as ex:
        return render(request, 'website/404.html', {'err': ex})


def service(request):
    try:
        __context = {}
        objService = Service.objects.filter(
            is_active=True).order_by('-pk')

        __context['MainServices'] = objService
        return render(request, 'website/services.html', __context)
    except Exception as ex:
        return render(request, 'website/404.html', {'err': ex})


def gallery(request):
    try:
        __context = {}
        objGallery = Gallery.objects.filter(
            is_active=True).order_by('-pk')

        __context['MainGallery'] = objGallery
        return render(request, 'website/gallery.html', __context)
    except Exception as ex:
        return render(request, 'website/404.html', {'err': ex})


def contact(request):
    try:
        __context = {}
    
        if request.method == 'POST':

            # req = contact(name=request.POST['name'],
            # email=request.POST['email'],
            # mobile_no=request.POST['mobile_no'],
            # subject=request.POST['subject'],
            # message=request.POST['message'])

            # req.save()

            form = ContactForm(request.POST, request.FILES)
            if form.is_valid():
               
                form.save()
                
                __context['success'] = 'We will call back to you soon!'
                form = ContactForm()
            
        else:
            form = ContactForm()

        __context['form'] = form

        return render(request, 'website/contact.html', __context)
    except Exception as ex:
        return render(request, 'website/404.html', {'err': ex})
