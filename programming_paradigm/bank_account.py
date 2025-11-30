class BankAccount:
	"""Simple BankAccount class demonstrating encapsulation and basic operations."""

	def __init__(self, initial_balance: float = 0.0):
		# account_balance is intended to be the internal state of the account
		self.account_balance = float(initial_balance)

	def deposit(self, amount: float) -> None:
		"""Add amount to the account balance.

		amount: positive numeric value to add to the balance.
		"""
		try:
			value = float(amount)
		except (TypeError, ValueError):
			raise ValueError("Invalid amount for deposit")
		self.account_balance += value

	def withdraw(self, amount: float) -> bool:
		"""Attempt to withdraw amount from the account.

		Returns True if successful, False if insufficient funds. Does not allow negative withdrawals.
		"""
		try:
			value = float(amount)
		except (TypeError, ValueError):
			raise ValueError("Invalid amount for withdraw")
		if value <= self.account_balance:
			self.account_balance -= value
			return True
		return False

	def display_balance(self) -> None:
		"""Print the current account balance in a friendly format."""
		print(f"Current Balance: ${self.account_balance:.2f}")

