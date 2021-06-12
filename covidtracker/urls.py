from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
