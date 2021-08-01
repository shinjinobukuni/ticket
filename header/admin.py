from django.contrib import admin

# Register your models here.
from .models import Header, Detail

admin.site.register(Header)
admin.site.register(Detail)