class LibraryBook:
    def __init__(self, isbn, title, author):
        self.__isbn = isbn
        self._title = title
        self._author = author

    def get_isbn(self):
        return self.__isbn

    def _display_basic_info(self):
        print(f"Title: {self._title}")
        print(f"Author: {self._author}")

# Example usage:
book1 = LibraryBook("978-0-19881984-4", "Python Crash Course", "Eric Matthes")
print(book1.get_isbn())  # Accessing the ISBN
book1._display_basic_info()  # Accessing the protected method