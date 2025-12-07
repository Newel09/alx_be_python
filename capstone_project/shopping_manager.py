def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def run_shopping_manager(groceries_budget: float):
    shopping_list = []
    print(f"You have ${groceries_budget:,.2f} available for groceries/shopping.\n")

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ").strip().lower()
            shopping_list.append(item)
            print(f"'{item.capitalize()}' has been added.\n")
        elif choice == '2':
            item = input("Enter the item to remove: ").strip().lower()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item.capitalize()}' has been removed.\n")
            else:
                print("Item not found in the list.\n")
        elif choice == '3':
            if not shopping_list:
                print("Your shopping list is empty.\n")
            else:
                print("Shopping List:")
                for item in shopping_list:
                    print(f"- {item.capitalize()}")
                print()
            print(f"Groceries budget: ${groceries_budget:,.2f}\n")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")
