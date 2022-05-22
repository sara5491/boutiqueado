from django.contrib import admin
from .models import Custom


class CustomAdmin(admin.ModelAdmin):
    """ Add contact form for admin backend """

    list_display = ('name', 'email', 'message',
                    'message_date',)
    
    readonly_fields = (
        'name', 'email', 'message',
        'message_date',
    )

    ordering = ('-message_date',)


admin.site.register(Custom, CustomAdmin)