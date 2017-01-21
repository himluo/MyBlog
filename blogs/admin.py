from django.contrib import admin
from blogs.models import Blog, Comment, Tag


class BlogAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
admin.site.register(Tag)