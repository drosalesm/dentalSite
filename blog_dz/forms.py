from django import forms
from .models import Post,Carrusel,Contact

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('__all__')


class CarruForm(forms.ModelForm):
    class Meta:
        model = Carrusel
        fields = ('__all__')

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('__all__')