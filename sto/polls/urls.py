from django.urls import path
from . import views
from .views import home_view


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('', home_view)
]