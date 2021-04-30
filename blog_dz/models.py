from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse


class User(AbstractUser):
    pass

    def __str__(self):
        return self.username


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    thumbnail = models.ImageField(verbose_name="Imagen")
    publish_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha publicación")
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(verbose_name="etiqueta", default='et')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={
            'slug': self.slug
        })


class Carrusel(models.Model):
    title = models.CharField(max_length=100, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    thumbnail = models.ImageField(verbose_name="Imagen")
    slug = models.SlugField(verbose_name="etiqueta")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detCarr", kwargs={
            'slug': self.slug
        })


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.user.username


class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Contact(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre")
    telefono = models.IntegerField(verbose_name="Numero de telefono")
    correo = models.EmailField(verbose_name="Correo")
    Mensaje = models.TextField(verbose_name="Mensaje")
    fecha = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
