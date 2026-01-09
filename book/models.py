from django.db import models

# title (заголовок) - CharField.
# author (автор) - CharField.
# description (опис) - TextField.
# price (ціна) - DecimalField.
# stock_count (кількість на складі) - IntegerField.
# published_date (дата публікації) - DateField.
# is_available (чи є в наявності) - BooleanField.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_count = models.IntegerField()
    published_date = models.DateField()
    is_available = models.BooleanField()

    def __str__(self):
        return f'"{self.title}", {self.author}'