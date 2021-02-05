from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth import settings

# Create your models here.


class Category(models.Model):
    objects = models.Manager

    name = models.CharField(max_length=150, unique=True)

    # Default Column Name
    is_active = models.BooleanField(default=True, editable=False)
    created_on = models.DateField(default=datetime.now, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, null=True, blank=True)
    modified_on = models.DateField(default=datetime.now, editable=False)

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"

    def __str__(self):
        return self.name


class Service(models.Model):
    objects = models.Manager

    name = models.CharField(max_length=150, unique=True)
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE, limit_choices_to={'is_active': True})
    icon = models.CharField(max_length=150, null=True, blank=True)
    thumbnail_image = models.ImageField(
        upload_to='services/', max_length=150, null=True, blank=True)
    short_content = models.TextField()

    # Default Column Name
    is_active = models.BooleanField(default=True, editable=False)
    created_on = models.DateField(default=datetime.now, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, null=True, blank=True)
    modified_on = models.DateField(default=datetime.now, editable=False)

    class Meta:
        verbose_name_plural = "Services"
        verbose_name = "Service"

    def __str__(self):
        return self.name


class ServiceDetails(models.Model):
    objects = models.Manager

    service = models.ForeignKey(Service,
                                on_delete=models.CASCADE, limit_choices_to={'is_active': True})
    url = models.SlugField(max_length=150, unique=True)
    long_content = models.TextField()

    # Default Column Name
    is_active = models.BooleanField(default=True, editable=False)
    created_on = models.DateField(default=datetime.now, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, null=True, blank=True)
    modified_on = models.DateField(default=datetime.now, editable=False)

    class Meta:
        verbose_name_plural = "Service Details"
        verbose_name = "Service Detail"

    def __str__(self):
        return self.service.name


class Gallery(models.Model):
    objects = models.Manager

    name = models.CharField(max_length=150, unique=True)

    # Default Column Name
    is_active = models.BooleanField(default=True, editable=False)
    created_on = models.DateField(default=datetime.now, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, null=True, blank=True)
    modified_on = models.DateField(default=datetime.now, editable=False)

    class Meta:
        verbose_name_plural = "Galleries"
        verbose_name = "Gallery"

    def __str__(self):
        return self.name


class GalleryDetails(models.Model):
    objects = models.Manager

    gallery = models.ForeignKey(Gallery,
                                on_delete=models.CASCADE, limit_choices_to={'is_active': True})
    name = models.CharField(max_length=150)
    image = models.ImageField(
        upload_to='gallery/', max_length=150)

    # Default Column Name
    is_active = models.BooleanField(default=True, editable=False)
    created_on = models.DateField(default=datetime.now, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, null=True, blank=True)
    modified_on = models.DateField(default=datetime.now, editable=False)

    class Meta:
        verbose_name_plural = "Gallery Details"
        verbose_name = "Gallery Details"

    def __str__(self):
        return self.name


class contact(models.Model):
    objects = models.Manager

    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150, null=True, blank=True)
    mobile_no = models.CharField(max_length=10)
    subject = models.CharField(max_length=150, default='')
    message = models.TextField(default='')

    # Default Column Name
    is_active = models.BooleanField(default=True, editable=False)
    created_on = models.DateField(default=datetime.now, editable=False)

    class Meta:
        verbose_name_plural = "Contact"
        verbose_name = "Contact"

    def __str__(self):
        return self.name