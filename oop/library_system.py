class Book:
    """Base Book class with common attributes."""

    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Electronic book with an additional file_size attribute (in KB)."""

    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = int(file_size)

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Printed book with an additional page_count attribute."""

    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = int(page_count)

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Library that composes Book instances and can list them."""

    def __init__(self):
        self.books = []

    def add_book(self, book: Book) -> None:
        """Add a Book, EBook or PrintBook to the library."""
        self.books.append(book)

    def list_books(self) -> None:
        """Print details of each book in the library."""
        for book in self.books:
            print(str(book))
