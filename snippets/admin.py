from django.contrib import admin

# Register your models here.

from snippets.models import *
admin.site.register(Snippet)
