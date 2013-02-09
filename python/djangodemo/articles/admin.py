from django.contrib import admin

from models import Articles


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'lastModify',)
    list_filter = ('created', 'lastModify',)
    ordering = ('title',)
    search_fields = ('title', 'text',)
    prepopulated_fields = {'url': ('title',)}


admin.site.register(Articles, ArticlesAdmin)

