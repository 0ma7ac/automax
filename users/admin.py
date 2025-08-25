from django.contrib import admin
from .models import Profile, Locations
# Register your models here.


class LocationAdmin(admin.ModelAdmin):
    pass
class ProfileAdmin(admin.ModelAdmin):
    pass



admin.site.register(Profile, ProfileAdmin)
admin.site.register(Locations,LocationAdmin)