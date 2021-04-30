from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from blog_dz import views


from blog_dz.views import(
#    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CarrListView,
    CarrCreateView,
    PostListado,
    logueo,
    CarrDetailView,
    CarrUpdateView,
    CarrDeleteView,
    ContactListView,
    ContactCreateView,
    sendEmail
)

urlpatterns = [
    path('login/', logueo,name='log'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', PostListado,name='list'),  
#    path('', PostListView.as_view(),name='list'),
    path('Carr', CarrListView.as_view(),name='Carr'),
    path('cont', ContactListView.as_view(),name='cont'),
    path('create/', PostCreateView.as_view(),name='create'),
    path('createC/', CarrCreateView.as_view(),name='createc'),
#   path('createCont/', ContactCreateView.as_view(),name='createCont'),
    path('createCont/', views.sendEmail,name='createCont'),
    path('<slug>/', PostDetailView.as_view(),name='detail'),
    path('carr/<slug>/', CarrDetailView.as_view(),name='detCarr'),
    path('update/<int:pk>', PostUpdateView.as_view(),name='update'),
    path('delete/<int:pk>', PostDeleteView.as_view(),name='delete'),
    path('carr/update/<int:pk>', CarrUpdateView.as_view(),name='updatecar'),
    path('carr/delete/<int:pk>', CarrDeleteView.as_view(),name='deletecar'),
]
#+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    