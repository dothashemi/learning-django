from django.contrib import admin
from articles.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'view', 'published', 'isActive')

    date_hierarchy = 'published'
    list_filter = ('published',)

    search_fields = ('title', 'body')

    actions = ['makeActive', 'makeDeactive']

    ordering = ['-published']

    # fields = ('title', 'body', 'published')
    # exclude = ('view',)
    fieldsets = (
        (None, {
            'fields': ('title', 'body', 'published')
        }),
        ('Advanced Options', {
            'classes': ('collapse',),
            'fields': ('view', 'isActive')
        })
    )

    def makeActive(self, request, queryset):
        rows = queryset.update(isActive=True)
        self.message(request, rows)

    def makeDeactive(self, request, queryset):
        rows = queryset.update(isActive=False)
        self.message(request, rows)

    makeActive.short_description = "Make Active"
    makeDeactive.short_description = "Make Deactive"

    def message(self, request, rows):
        if rows == 1:
            message = '1 Article was Updated.'
        else:
            message = '%s Articles were Updated.' % rows

        self.message_user(request, message)
