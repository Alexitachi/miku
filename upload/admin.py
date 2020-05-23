from django.contrib import admin
from .models import Book,Profile,Topic,Entry,Query

# Register your models here.


admin.site.register(Profile)
admin.site.register(Book)
admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Query)