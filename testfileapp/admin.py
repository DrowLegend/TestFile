from django.contrib import admin
from testfileapp.models import UploadFile

# Register your models here.


class UploadFileAdmin(admin.ModelAdmin):
    list_display = ('file', 'author', 'date')
    list_per_page = 10
    list_filter = ('file', 'author', 'date')


admin.site.register(UploadFile, UploadFileAdmin)