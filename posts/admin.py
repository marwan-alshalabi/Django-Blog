from django.contrib import admin

from .models import Post

class postAdmin(admin.ModelAdmin):
    list_display=['id','name','created_at']
    list_filter=['created_at','tags']
    search_fields=['name','content']

admin.site.register(Post,postAdmin)
