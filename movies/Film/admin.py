from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Film)
admin.site.register(Genere)
admin.site.register(Attore)
admin.site.register(Regista)