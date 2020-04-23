from django.contrib import admin

from crm.models import Customer, CustomerNote, ImageFile


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user',
        'first_name',
        'last_name',
        'phone',
        'country',
    ]
    list_filter = ['user', 'country']


@admin.register(ImageFile)
class ImageFileAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'file',
        'user',
    ]

    list_filter = ['user']


@admin.register(CustomerNote)
class CustomerNoteAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'customer',
    ]

    list_filter = ['customer', 'customer__user']
