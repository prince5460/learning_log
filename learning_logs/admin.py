from django.contrib import admin

# Register your models here.
from learning_logs.models import Topic,Entry


class ll_admin(admin.ModelAdmin):
    list_display = ('text', 'date_added')
    search_fields = ('topic','text')
    list_filter = ['date_added',]


admin.site.register(Topic,ll_admin)
admin.site.register(Entry)
