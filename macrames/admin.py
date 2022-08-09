from django.contrib import admin
from .models import Macrame, Category


class MacrameAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('-price',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Macrame, MacrameAdmin)
admin.site.register(Category, CategoryAdmin)
