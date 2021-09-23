from django.contrib import admin
from .models import Person
from .models import Name

#admin.site.register(Person)
admin.site.register(Name)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'name', 'address')
    ordering = ('nickname',)
    search_fields = ('name', 'address')