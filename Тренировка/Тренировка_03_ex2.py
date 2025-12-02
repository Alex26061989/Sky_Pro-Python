from Тренировка_03_book import Book

library = [
    Book("Чёрный принц", "Айрис Мёрдок"),
    Book("Апельсиновая девушка", "Юстейн Гордер"),
    Book("Тепло наших тел", "Айзек Марион")
]

for book in library:
    print(f"{book.title} - {book.author}")