from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth import settings


class Category(models.Model):
    objects = models.Manager
    name = models.CharField(max_length=200)


class Investigation_Category(models.Model):
    objects = models.Manager
    name = models.CharField(max_length=150)
    status = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, null=True, blank=True)
    created_on = models.DateField(default=datetime.now, editable=False)

    class Meta:
        verbose_name_plural = "Investigation_Category"
        verbose_name = "Investigation_Category"
    def __str__(self):
        return self.name


class Investigation(models.Model):
    objects = models.Manager

    name = models.CharField(max_length=150)
    amount = models.CharField(max_length=50)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, null=True, blank=True)
    created_on = models.DateField(default=datetime.now, editable=False)

    class Meta:
        verbose_name_plural = "Investigation"
        verbose_name = "Investigation"
    def __str__(self):
        return self.name




class Registration(models.Model):
    objects = models.Manager 
    gender=(
        ('Male','Male'),
        ('Female','Female'),
    )
    name = models.CharField(max_length=150)
    age = models.CharField(max_length=50)
    gender = models.CharField(max_length=100, choices=gender, verbose_name='gender')
    consuitant_no = models.CharField(max_length=200)
    uhid_no = models.CharField(max_length=200)
    lab_no = models.CharField(max_length=50)
    reference_if_age = models.CharField(max_length=300)
    investigation = models.ForeignKey(Investigation, on_delete=models.CASCADE, null=True, blank=True)


    is_active = models.BooleanField(default=True, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, null=True, blank=True)
    created_on = models.DateField(default=datetime.now, editable=False)
    class Meta:
        verbose_name_plural = "Registrations"
        verbose_name = "Registration"
    def __str__(self):
        return self.name

class RegistrationDetails(models.Model):

    objects = models.Manager
    name = models.CharField(max_length=200)
    registration = models.ForeignKey(Registration, on_delete=models.CASCADE,limit_choices_to={'is_active': True})
    amount = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = "RegistrationDetails"
        verbose_name = "RegistrationDetails"
    def __str__(self):
        return self.name

# class patient(models.Model):
#     objects = models.Manager
    
#     registration = models.ForeignKey(Registration, on_delete=models.CASCADE, limit_choices_to={'is_active':True})
#     investigation = models.ForeignKey(Investigation, on_delete=models.CASCADE, limit_choices_to={'is_active':True})



class Doctor(models.Model):
    objects = models.Manager
    name = models.CharField(max_length=150)
    mobile_no = models.CharField(max_length=200)
    status = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, null=True, blank=True)
    created_on = models.DateField(default=datetime.now, editable=False)
    class Meta:
        verbose_name_plural = "doctor"
        verbose_name = "doctor"
    def __str__(self):
        return self.name


class User(models.Model):
    objects = models.Manager
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=200)
    status = models.BooleanField(default=True)

    is_active = models.BooleanField(default=True, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, null=True, blank=True)
    created_on = models.DateField(default=datetime.now, editable=False)
    class Meta:
        verbose_name_plural = "user"
        verbose_name = "user"
    def __str__(self):
        return self.name