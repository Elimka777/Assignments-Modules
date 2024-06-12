# main.py
import text_utils as tu

def main():
    while True:
        print("\nString Manipulation Utility")
        print("1. Reverse String")
        print("2. Capitalize String")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            s = input("Enter the string to reverse: ")
            print(f"Reversed String: {tu.reverse_string(s)}")
        elif choice == '2':
            s = input("Enter the string to capitalize: ")
            print(f"Capitalized String: {tu.capitalize_string(s)}")
        elif choice == '3':
            print("Exiting String Manipulation Utility.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
