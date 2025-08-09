from django.contrib import admin
from blog_post.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ("post_name", "created_by", "post_date" )
    prepopulated_fields = {"slug_link" : ("post_name",)}
    
    
admin.site.site_header = "Xtra-Dose Admin Panel"
admin.site.site_title = "Xtra-Dose Admin"
admin.site.index_title = "Welcome to the Xtra-Dose Dashboard"
    
    
# Register your models here.
admin.site.register(Post, PostAdmin)