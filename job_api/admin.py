from django.contrib import admin
from .models.user import User
from .models.job import Job

# Register your models here.
admin.site.register(User)
admin.site.register(Job)
