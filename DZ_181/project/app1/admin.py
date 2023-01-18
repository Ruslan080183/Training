from django.contrib import admin
from .models import Genre, Film, Viewer

admin.site.register(Genre)
admin.site.register(Film)
admin.site.register(Viewer)