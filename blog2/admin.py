from django.contrib import admin

from blog.models import Post
# from blog.models import Post
from .models import *

# Register your models here.

admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(ResenPost)
admin.site.register(InstagramPost)
admin.site.register(Newsletter)
admin.site.register(Blog_detail)
admin.site.register(Comment)
