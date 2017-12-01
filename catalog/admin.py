from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

# Register your models here.
admin.site.register(Genre)
admin.site.register(Language)
#admin.site.register(Book)
#admin.site.register(BookInstance)
#admin.site.register(Author)

class BookInline(admin.TabularInline):
    model = Book
    extr = 0

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    #controls what the list view looks like
    list_display = ('last_name','first_name','date_of_birth','date_of_death')
    #this controls what the details view looks like. eg. when you view one author or add a new author
    fields = ['first_name', 'last_name', ('date_of_birth','date_of_death')]
    inlines = [BookInline]

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    #Stop population of book instances that are not intances of the selected book
    extra = 0

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','display_genre')
    inlines = [BooksInstanceInline]

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book','status','due_back','id')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book','imprint','id')
        }),
        ('Availability', {
            'fields': ('status','due_back')
        }),
    )
