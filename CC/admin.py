from django.contrib import admin
from .models import CrownsPost

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('BrandName','Slug','Status','Created_on')
    list_filter = ['Status']
    search_fields = ['BrandName','Content']
    prepopulated_fields = {'Slug':('BrandName',)}

admin.site.register(CrownsPost,PostAdmin)

#CrownsCollections
#cc2020