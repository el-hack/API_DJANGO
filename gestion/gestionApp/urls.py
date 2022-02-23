from django.urls import path
from . import views
urlpatterns = [
    path('clients/',views.allClients),
    path('client/<int:id>/',views.getClient),
]