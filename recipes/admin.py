from django.contrib import admin
from .models import Recipe, Comment, Rating
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_at', 'updated_at')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register your models here.
admin.site.register(Comment)
admin.site.register(Rating)