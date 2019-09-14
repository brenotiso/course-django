from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Publication
from .forms import Publication_Admin


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date']

    form = Publication_Admin

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

# Removendo o Model Group da listagem. Não é utilizado.
admin.site.unregister(Group)
