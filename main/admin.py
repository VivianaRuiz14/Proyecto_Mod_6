from django.contrib import admin
from main.models import contacto, Flan


class mainAdmin(admin.ModelAdmin):
  pass

admin.site.register(contacto, mainAdmin)
class FlanAdmin(admin.ModelAdmin):
    pass

admin.site.register(Flan, FlanAdmin)