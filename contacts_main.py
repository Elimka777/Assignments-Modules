# main.py
import contacts_manager

def main():
    while True:
        print("\nContact List Manager")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Display Contacts")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            print(contacts_manager.add_contact(name, phone))
        elif choice == '2':
            name = input("Enter name to remove: ")
            print(contacts_manager.remove_contact(name))
        elif choice == '3':
            print("Contact List:")
            print(contacts_manager.display_contacts())
        elif choice == '4':
            print("Exiting Contact List Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()