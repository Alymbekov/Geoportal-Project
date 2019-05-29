from django.contrib.gis import admin
from .models import WorldBorder, Post, Tag, Comment
from apps.users.models import User

admin.site.register(WorldBorder, admin.GeoModelAdmin)
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)
