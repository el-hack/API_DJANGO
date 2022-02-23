from multiprocessing.connection import Client
from django.contrib import admin
from .models import Client , Service , Typeabo
# Register your models here.
admin.site.register(Client)
admin.site.register(Service)
admin.site.register(Typeabo)
