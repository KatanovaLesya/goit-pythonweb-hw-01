import logging
from abc import ABC, abstractmethod
from typing import List

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


class LibraryInterface(ABC):
    """Інтерфейс бібліотеки"""

    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def show_books(self) -> None:
        pass


class Library(LibraryInterface):
    """Клас бібліотеки, який реалізує LibraryInterface"""

    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        logging.info(f"Книга '{book.title}' додана до бібліотеки.")

    def remove_book(self, title: str) -> None:
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                logging.info(f"Книга '{title}' була видалена.")
                return
        logging.warning(f"Книга '{title}' не знайдена в бібліотеці.")

    def show_books(self) -> None:
        if not self.books:
            logging.info("Бібліотека порожня.")
        else:
            for book in self.books:
                logging.info(book)
