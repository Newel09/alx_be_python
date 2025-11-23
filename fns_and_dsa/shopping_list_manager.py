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
            print("Enter the item to add:")
            item = input()
            shopping_list.append(item.capitalize())
        elif choice == '2':
            print("Enter the item to remove:")
            item = input()
            if item.capitalize() in shopping_list:
                shopping_list.remove(item.capitalize())
            else:
                print("Item not found in the list.")
        elif choice == '3':
            print("Shopping List:")
            for item in shopping_list:
                print(f"- {item}")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()