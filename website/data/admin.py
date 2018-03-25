from django.contrib import admin
from .models import PagesLiked
from django.contrib.admin import register, ModelAdmin
from django.db import models
from django.forms import TextInput, Textarea
from django.utils.html import format_html

# Register your models here.


class PagesLikedadmin(admin.ModelAdmin):
   formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 5, 'cols': 60})},
    }

admin.site.register(PagesLiked, PagesLikedadmin)