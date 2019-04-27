from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Profile)
admin.site.register(PrivateChat)
admin.site.register(GroupChat)
admin.site.register(Message)
admin.site.register(GroupMessage)
admin.site.register(PrivateMessage)