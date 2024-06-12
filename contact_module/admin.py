from django.contrib import admin
from .models import ContactUs
import pytz


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'jtimestamp', 'is_called')
    list_filter = ['is_called']

    def jtimestamp(self, obj):
        local_time = obj.timestamp.astimezone(pytz.timezone('Asia/Tehran'))
        return local_time.strftime('%Y-%m-%d %H:%M')

    jtimestamp.short_description = 'تاریخ ایجاد (شمسی)'


admin.site.register(ContactUs, ContactUsAdmin)
