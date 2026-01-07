from django.contrib import admin
from favourite.models import Favourite
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Favourite)
class FavouriteAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)