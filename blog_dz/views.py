from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment, User, Like, Carrusel, Contact
from .forms import PostForm, CarruForm, ContactForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.mail import send_mail,EmailMessage
from django.http import HttpResponse, HttpResponseRedirect


# Vistas para POST

# class PostListView(ListView):
#    model=Post

def PostListado(request):
    post = Post.objects.all().order_by('-last_updated')
    slider = Carrusel.objects.all
    return render(request, 'blog_dz/post_list.html', {"post": post, "slider": slider})


def logueo(request):
    return render(request, 'blog_dz/login.html')


class PostDetailView(DetailView):
    model = Post


@method_decorator(login_required, name='dispatch')
class PostCreateView(CreateView):
    form_class = PostForm
    model = Post
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'create'
        })
        return context

@method_decorator(login_required, name='dispatch')
class PostUpdateView(UpdateView):
    form_class = PostForm
    model = Post
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'update'
        })
        return context

@method_decorator(login_required, name='dispatch')
class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'


# Vistas para el CARRUSEL
class CarrListView(ListView):
    model = Carrusel


class CarrDetailView(DetailView):
    model = Carrusel

@method_decorator(login_required, name='dispatch')
class CarrUpdateView(UpdateView):
    form_class = CarruForm
    model = Carrusel
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'update'
        })
        return context

@method_decorator(login_required, name='dispatch')
class CarrDeleteView(DeleteView):
    model = Carrusel
    success_url = '/'

@method_decorator(login_required, name='dispatch')
class CarrCreateView(CreateView):
    form_class = CarruForm
    model = Carrusel
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'create'
        })
        return context

# Vista para el fomulario de contacto

class ContactListView(ListView):
    model = Contact

class ContactCreateView(CreateView):
    form_class = ContactForm
    model = Contact
    success_url = '/'
    def sendEmailContact(request):
        if request.method=='POST':
            print("Hola")
        return redirect('/')


def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context.update({
        'view_type': 'create'
    })
    return context



# Vista para envio de EMAIL
def sendEmail(request):
    if request.method=='GET':
        form = ContactForm()
        contexto={
            'form':form
            }
    else:
        form=ContactForm(request.POST)
        contexto={
            'form':form
        }
        if form.is_valid():
           consult = request.POST.get('Mensaje')
           telefono= request.POST.get('telefono')
           pers= request.POST.get('nombre')
           corr= request.POST.get('correo')
           form.save()
           send_mail(
                'Consulta medica dental',
                pers+' tiene la siguiente consulta: '+consult+' El numero telefonico del cliente es: '+telefono+' El correo electronico del cliente es: '+corr,
                'consultas@gmail.com',
                ['doctoradevrazunigahn@gmail.com'],
                fail_silently=False,
            )
        send_mail(
                'Consulta medica dental',
                'Hola '+pers+' he recibido tu mensaje, te contactare lo mas pronto posible',
                'consultas@gmail.com',
                [corr],
                fail_silently=False,
        )
        return redirect('/')
    return render(request,'contacto.html',contexto)