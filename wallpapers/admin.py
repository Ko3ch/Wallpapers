from django.contrib import admin
from . models import category,location,Image

admin.site.register(category)
admin.site.register(location)
admin.site.register(Image)