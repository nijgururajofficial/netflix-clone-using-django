from django.contrib import admin
from netflixapp.models import *

# Register your models here.

admin.site.register(Movie)
admin.site.register(Video)
admin.site.register(Profile)
admin.site.register(CustomUser)