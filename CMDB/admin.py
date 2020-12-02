from django.contrib import admin
from .models import AsSet, Manufacturer, Room, House, User
# Register your models here.
admin.site.register(AsSet)
admin.site.register(Manufacturer)
admin.site.register(Room)
admin.site.register(House)
admin.site.register(User)