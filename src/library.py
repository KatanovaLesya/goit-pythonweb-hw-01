import logging
from typing import List  # Для типізації списку книг

# Налаштування логування
logging.basicConfig(level=logging.INFO)

class Book:
    """Клас, що представляє книгу"""

    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        """Форматований вивід інформації про книгу"""
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class Library:
    """Клас бібліотеки, який зберігає книги"""

    def __init__(self):
        self.books: List[Book] = []  # Тепер тут список об'єктів Book

    def add_book(self, book: Book) -> None:
        """Додає книгу в бібліотеку"""
        self.books.append(book)
        logging.info(f"Книга '{book.title}' додана до бібліотеки.")

    def remove_book(self, title: str) -> None:
        """Видаляє книгу за назвою"""
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                logging.info(f"Книга '{title}' була видалена.")
                return
        logging.warning(f"Книга '{title}' не знайдена в бібліотеці.")

    def show_books(self) -> None:
        """Виводить всі книги в бібліотеці"""
        if not self.books:
            logging.info("Бібліотека порожня.")
        else:
            for book in self.books:
                logging.info(book)  # Використовує __str__ для форматованого виводу
