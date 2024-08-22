# albums/admin.py
from django.contrib import admin
from .models import Album, Song, Singer, Writer

admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Singer)
admin.site.register(Writer)
