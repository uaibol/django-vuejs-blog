from django.contrib import admin
from .models import Post, Category, Tag, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_date', 'status', 'comment_status' ,'slug', 'view_count']

    class Meta:
        model = Post

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'order']

    class Meta:
        model = Category

class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']

    class Meta:
        model = Tag

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name']

    class Meta:
        model = Comment

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
