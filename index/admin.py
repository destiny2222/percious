from django.contrib import admin
from index.models import *

# Register your models here.
class homeAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'slug']
    list_filter = ['title', 'date']
    list_display_links = ['title', 'date'
    ]
    prepopulated_fields={'slug':['title']}

admin.site.register(home, homeAdmin)
