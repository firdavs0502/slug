from django.urls import path
from .views import home , detal

urlpatterns = [
    path('', home),
    path('<slug:slug>/', detal, name='detal'),
]