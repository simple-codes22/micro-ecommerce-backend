from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

class CustomAdmin(UserAdmin):
    model = CustomUser
    search_fields = ("email",)
    # ordering = ("email",)

admin.site.register([CustomUser,], CustomAdmin)
admin.site.register([Product, Order, ProductImage, Review])
