from django.contrib import admin

# Register your models here.
from .models import Request, Question

admin.site.register(Request)
admin.site.register(Question)
