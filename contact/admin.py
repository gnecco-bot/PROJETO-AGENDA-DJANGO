from django.contrib import admin
from contact import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', 'email', 'created_date')
    ordering = 'id',
    # list_filter = 'created_date',
    search_fields = 'first_name', 'last_name', 'phone', 'email',
    list_per_page = 10
    list_max_show_all = 200
    list_editable = 'phone', 'email',
    list_display_links = 'id', 'first_name',