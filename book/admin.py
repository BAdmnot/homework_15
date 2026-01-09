# Відображення (list_display): Виведіть у загальний список  назву, автора, ціну, дату публікації та статус наявності.
# Фільтрація (list_filter): Налаштуйте бічну панель фільтрів за полями is_available та published_date.
# Пошук (search_fields) : Реалізуйте пошук за назвою книги та описом. Перевірте, як працює пошук, якщо ввести лише частину імені.
# Логіка сортування (ordering): Встановіть сортування за замовчуванням так, щоб нові книги (за датою публікації) завжди відображалися на початку списку. Якщо дати однакові - сортуйте за алфавітом (за назвою).
# Захист даних (readonly_fields): Уявіть, що ціна та дата публікації - це критичні дані, які не можна змінювати після створення запису (або вони мають бути захищені від випадкового редагування). Зробіть поля price та published_date доступними лише для читання.

from django.contrib import admin

from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "price", "published_date", "is_available")
    search_fields = ("title", "description")
    list_filter = ("is_available", "published_date")
    ordering = ("-published_date", "title")
    readonly_fields = ("price", "published_date")

admin.site.register(Book, BookAdmin)