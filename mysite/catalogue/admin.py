from django.contrib import admin

from .models import Author, Book, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description_preview")
    search_fields = ("name", "description")

    @admin.display(description="Apercu")
    def description_preview(self, obj):
        return obj.description[:60]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "category", "price", "publication_date")
    search_fields = ("title", "summary")
    list_filter = ("publication_date", "author", "category")


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "email", "joined_date")
    search_fields = ("last_name", "email")
