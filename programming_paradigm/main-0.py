import sys
from bank_account import BankAccount


def main():
    # Example starting balance; adjust as needed
    account = BankAccount(100)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Parse command and optional parameter
    parts = sys.argv[1].split(":")
    command = parts[0].lower()
    amount = None
    if len(parts) > 1 and parts[1] != "":
        try:
            amount = float(parts[1])
        except ValueError:
            print("Invalid amount. Please provide a numeric value.")
            sys.exit(1)

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")


if __name__ == "__main__":
    main()
