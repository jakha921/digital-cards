from django.contrib import admin
from django.utils.html import format_html

from app.models import Client, Button


# Register your models here.
class ClientAdmin(admin.TabularInline):
    model = Client
    extra = 0
    readonly_fields = ('get_avatar',)

    def get_avatar(self, obj):
        return format_html(f'<img src="{obj.avatar_url}" width="100" height="100"')

    get_avatar.short_description = 'Аватар'


class ButtonAdmin(admin.StackedInline):
    model = Button
    extra = 1


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'fullname', 'dob', 'title', 'get_avatar')
    list_display_links = ('nickname',)
    search_fields = ('fullname', 'nickname', 'position')
    readonly_fields = ('get_avatar',)
    inlines = [ButtonAdmin]

    def get_avatar(self, obj):
        return format_html(f'<img src="{obj.avatar.url}" width="100" height="100"')

    get_avatar.short_description = 'Аватар'

#
# @admin.register(Button)
# class ButtonAdmin(admin.ModelAdmin):
#     list_display = ('link', 'color', 'text', 'sub_text', 'client')
#     list_display_links = ('link', 'color', 'text', 'sub_text')
#     search_fields = ('link', 'color', 'text', 'sub_text')
#     list_filter = ('client',)
