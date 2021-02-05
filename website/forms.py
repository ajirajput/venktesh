from django import forms
from .models import contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = "__all__"

    def __init__(self, *args, **kw):
        super(ContactForm, self).__init__(*args, **kw)
