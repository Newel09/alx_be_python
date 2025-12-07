class Book:
	"""Represents a book and demonstrates Python magic methods.

	Attributes:
		title (str): Book title
		author (str): Book author
		year (int): Publication year
	"""

	def __init__(self, title: str, author: str, year: int):
		self.title = title
		self.author = author
		self.year = int(year)

	def __del__(self):
		# Called when the object is about to be destroyed
		print(f"Deleting {self.title}")

	def __str__(self) -> str:
		return f"{self.title} by {self.author}, published in {self.year}"

	def __repr__(self) -> str:
		return f"Book('{self.title}', '{self.author}', {self.year})"

