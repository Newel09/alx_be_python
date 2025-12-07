def get_monthly_income():
    while True:
        try:
            value = float(input("Enter your monthly income: ").strip())
            if value < 0:
                print("Please enter a non-negative number for income.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value for income.")


def get_allocations():
    categories = [
        ("investment", "Investment (long-term)"),
        ("savings", "Savings (short-term)"),
        ("groceries", "Groceries"),
        ("transportation", "Transportation"),
        ("tithe", "Tithe"),
    ]

    while True:
        allocations = {}
        print("\nPlease allocate percentages for the following categories so they add up to 100%:")
        total = 0.0
        for key, label in categories:
            while True:
                try:
                    raw = input(f"- {label}: ").strip()
                    pct = float(raw)
                    if pct < 0:
                        print("Please enter a non-negative percentage.")
                        continue
                    allocations[key] = pct
                    total += pct
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric percentage (e.g. 10 or 12.5).")

        if abs(total - 100.0) > 0.0001:
            print(f"The total is {total:.2f}%. The allocations must sum to 100%. Please try again.\n")
            continue

        return allocations


def compute_amounts(income, allocations):
    # returns a dict with monetary amounts for each category
    return {
        "investment": income * (allocations.get("investment", 0.0) / 100.0),
        "savings": income * (allocations.get("savings", 0.0) / 100.0),
        "groceries": income * (allocations.get("groceries", 0.0) / 100.0),
        "transportation": income * (allocations.get("transportation", 0.0) / 100.0),
        "tithe": income * (allocations.get("tithe", 0.0) / 100.0),
    }
