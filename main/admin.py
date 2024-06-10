from django.contrib import admin
from main.models import contacto

class mainAdmin(admin.ModelAdmin):
  pass

admin.site.register(contacto, mainAdmin)