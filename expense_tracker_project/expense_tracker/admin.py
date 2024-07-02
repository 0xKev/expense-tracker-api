from django.contrib import admin
from accounts.models import CustomUser
from .models import *

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Expense)