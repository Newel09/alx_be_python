def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt, trim whitespace and store in lowercase
            item = input("Enter the item to add: ").strip().lower()
            shopping_list.append(item)
            print(f"'{item.capitalize()}' has been added.\n")
        elif choice == '2':
            # Prompt and normalize input in one call (trim + lowercase)
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
                    # Display with capitalization while keeping storage lowercase
                    print(f"- {item.capitalize()}")
                print()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()