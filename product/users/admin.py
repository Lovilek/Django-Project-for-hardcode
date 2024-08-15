from django.contrib import admin
from .models import Subscription,Balance,CustomUser
admin.site.register(CustomUser)

admin.site.register(Balance)
admin.site.register(Subscription)