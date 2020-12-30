from django.contrib import admin
from articles.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'view', 'published')

    date_hierarchy = 'published'
    list_filter = ('published',)

    search_fields = ('title', 'body')

    ordering = ['-published']

    # fields = ('title', 'body', 'published')
    # exclude = ('view',)
    fieldsets = (
        (None, {
            'fields': ('title', 'body', 'published')
        }),
        ('Advanced Options', {
            'classes': ('collapse',),
            'fields': ('view',)
        })
    )
