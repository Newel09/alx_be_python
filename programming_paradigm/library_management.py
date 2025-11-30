class Book:
	"""Represents a book with title, author and availability state."""

	def __init__(self, title: str, author: str):
		self.title = title
		self.author = author
		self._is_checked_out = False

	def check_out(self) -> bool:
		"""Mark the book as checked out. Return True if successful, False if already checked out."""
		if self._is_checked_out:
			return False
		self._is_checked_out = True
		return True

	def return_book(self) -> bool:
		"""Return the book. Return True if successful, False if it was not checked out."""
		if not self._is_checked_out:
			return False
		self._is_checked_out = False
		return True

	def is_available(self) -> bool:
		"""Return True if the book is available for checkout."""
		return not self._is_checked_out

	def __str__(self) -> str:
		return f"{self.title} by {self.author}"


class Library:
	"""Simple library managing a collection of Book instances."""

	def __init__(self):
		self._books = []

	def add_book(self, book: Book) -> None:
		"""Add a Book instance to the library collection."""
		self._books.append(book)

	def _find_book_by_title(self, title: str):
		"""Return the Book with matching title or None if not found (case-sensitive)."""
		for book in self._books:
			if book.title == title:
				return book
		return None

	def check_out_book(self, title: str) -> bool:
		"""Attempt to check out a book by title. Return True on success, False otherwise."""
		book = self._find_book_by_title(title)
		if book is None:
			return False
		return book.check_out()

	def return_book(self, title: str) -> bool:
		"""Attempt to return a book by title. Return True on success, False otherwise."""
		book = self._find_book_by_title(title)
		if book is None:
			return False
		return book.return_book()

	def list_available_books(self) -> None:
		"""Print all available (not checked out) books, one per line."""
		for book in self._books:
			if book.is_available():
				print(str(book))

