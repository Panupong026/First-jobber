from django.contrib import admin
from .models import Insurance, User, Coverage

# Register your models here.

admin.site.register(Insurance)
admin.site.register(User)
admin.site.register(Coverage)