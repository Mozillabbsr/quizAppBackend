from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(UserDetail)
admin.site.register(Quiz)
admin.site.register(Questions)
admin.site.register(Attend)
admin.site.register(Tags)