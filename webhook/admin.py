from django.contrib import admin

from webhook.models import Webhook


@admin.register(Webhook)
class WebookAdmin(admin.ModelAdmin):
    readonly_fields = ('date', 'rehook_id', )
