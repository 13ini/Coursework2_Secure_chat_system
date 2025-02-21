import os

def main():
    print("Choose a client:")
    print("1. GUI Client")
    print("2. CLI Client")

    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        os.system('python gui_client.py')
    elif choice == '2':
        os.system('python cli_client.py')
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
