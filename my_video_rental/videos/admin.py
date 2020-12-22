from django.contrib import admin

# Register your models here.


from . import models


class MovieAdmin(admin.ModelAdmin): #m aodelname+'admin'

    fields = ['release_year','title','length']  # title,length,release year is the original order



admin.site.register(models.Customer)
admin.site.register(models.Movie,MovieAdmin)
