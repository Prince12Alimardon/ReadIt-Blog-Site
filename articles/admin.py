from django.contrib import admin
from .models import Tag, Category, Article, Comment


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title', )


class CommentInlineAdmin(admin.StackedInline):
    model = Comment
    extra = 0


class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInlineAdmin]
    list_display = ('id', 'author', 'title', 'category', 'created_at')
    list_filter = ('created_at', 'updated_at', 'tags')
    search_fields = ('title', )
    readonly_fields = ('updated_at', 'created_at')
    prepopulated_fields = ({'slug': ('title', )})
    filter_horizontal = ('tags', )


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'article', 'name', 'email', 'created_at')
    list_filter = ('created_at', )
    readonly_fields = list_filter
    search_fields = ('name', 'email',)


admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
