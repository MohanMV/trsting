from django.contrib import admin
from .models import Post

# to make Post model(table, database) visible in admin page
admin.site.register(Post)
