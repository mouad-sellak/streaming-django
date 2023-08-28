import profile
from django.contrib import admin

# import video

# Register your models here.
from .models import Episode, Film,Serie, Music,Documentaire
from .models import *

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user','review','rating'] #film__title

# admin.site.register(Video)
admin.site.register(Film)
admin.site.register(Serie)
admin.site.register(Music)
admin.site.register(Documentaire)
admin.site.register(Episode)
admin.site.register(Favorite)
admin.site.register(WatchLater)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(ReviewRating,ReviewAdmin)
admin.site.register(Chaine)
admin.site.register(HistoriqueVisionnage)


