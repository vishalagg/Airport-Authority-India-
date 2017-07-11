from django.contrib import admin
from .models import CargoPlane, InternationalPlane, LocalPlane, Emergency

class Limitation(admin.ModelAdmin):
  def has_add_permission(self, request):
    num_objects = self.model.objects.count()
    if num_objects >= 15:
      return False
    else:
      return True

class Limitation_E(admin.ModelAdmin):
  def has_add_permission(self, request):
    num_objects = self.model.objects.count()
    if num_objects >= 5:
      return False
    else:
      return True

admin.site.register(CargoPlane,Limitation)
admin.site.register(InternationalPlane,Limitation)
admin.site.register(Emergency,Limitation_E)
admin.site.register(LocalPlane,Limitation)