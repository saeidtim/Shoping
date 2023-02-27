from django.contrib import admin
from .models import Book, Comment

@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    list_display = ('user', 'title', 'datetime_created', )
    list_filter = ('datetime_created', )


@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    list_filter = ('text', )