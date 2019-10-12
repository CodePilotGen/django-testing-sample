from django.contrib import admin
from main.apps.magazine.models import NewsArticle

@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    pass

