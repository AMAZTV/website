from django.contrib import admin
from amaztv_app.models import Posts #, Data

class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'category', 'id')

admin.site.register(Posts, PostsAdmin)
#admin.site.register(Data)
