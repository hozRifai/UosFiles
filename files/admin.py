from django.contrib import admin
# Register your models here.
from .models import CoursesNames  , Document


admin.site.register(CoursesNames)

admin.site.register(Document)

