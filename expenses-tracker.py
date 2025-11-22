#!/usr/bin/python3

#reads the balance from balance.txt and returns it 
def read_balance():
    with open("balance.txt", "r") as file:
        balance = file.read().strip()
        return float(balance)
# writes a new balance to balance.txt 
def write_balance(new_balance):
    with open("balance.txt", "w") as file:
        file.write(str(new_balance))

# Calculates the total of expenses
import os

def calculate_total_expenses():
    total = 0

    for file in os.listdir():
        if file.startswith("expenses_") and file.endswith(".txt"):
            with open(file, "r") as f:
                for line in f:
                    parts = line.split(" - ")  
                    amount = float(parts[1])   
                    total += amount
    return total

# Shows current balance 
def check_balance():
    balance = read_balance()
    total_expenses = calculate_total_expenses()

    available = balance - total_expenses

    print("\n===CHECK REMAINING BALANCE===")
    print(f"Current balance:{balance}")
    print(f"Total Expenses:{total_expenses}")
    print(f"Available Balance:{available}")

    choice = input("Do you want to add money?(y/n):").lower()
    if choice == "y":
        amount = input("ENter amount to add:")
        if amount.isdigit() and float(amount)>0:
            new_balance = balance + float(amount)
            write_balance(new_balance)
            print(f"New Balance:{new_balance}")
        else:
            print("Invalid amount!")

#Adds a new expense to the correct expense file
def add_expense():
    print("\n===ADD NEW EXPENSE===")

    balance = read_balance()
    print(f"Available Balance: {balance}")

    date =input("Enter date(YYY-MM-DD):")

    filename= f"expenses_{date}.txt"

    item = input("Enter item name: ")
    amount = input("Enter amount spent: ")

    if not amount.replace('.','', 1).isdigit() or float(amount) <=0:
        print("invalid amount! Must be a positive number.")
        return
    
    print("\n You entered:")
    print(f"Date: {date}")
    print(f"Item:{item}")
    print (f"Amount:{amount}")
    confirm = input("Confirm? (y/n):").lower()
    
    if confirm != "y":
        print("Expense cancelled.")
        return
    if float(amount) > balance:
        print("Insufficient balance! cannot save expense.")
        return
    
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            next_id = len(lines) + 1
    except FileNotFoundError:
        next_id = 1

    from datetime import datetime
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filename, "a") as file:
        file.write(f"{next_id}. {item} - {amount} - {now}\n")

    new_balance = balance - float(amount)
    write_balance(new_balance)

    print(f"Expense saved successfully! New balance: {new_balance}")
  
  # shows  expenses for a specific date
def view_expenses():
    print("\n=== VIEW EXPENSES===")
    date =input("Enter the date (YYYY-MM-DD): ")
    filename = f"expenses_{date}.txt"

    try:
        with open(filename, "r") as file:
            print("\nExpenses for", date)
            print("------------------------")
            for line in file:
                print(line.stript())
    except FileNotFoundError:
        print("No expenses found for that date Sorry!.")

#Shows submenu to search expenses
def view_expenses_menu():
    print("\n====VIEW EXPENSES===")
    print("1. Search by item name")
    print("2. Search by amount")
    print("3. Back to main menu")

    choice =input("Enter your choice(1-3):")
    return choice

#Searches for an item name inside a date file
def search_by_item():
    print("\n===SEARCH BY ITEM NAME===")

    date = input("Enter date(YYYY-MM-DD): ")
    filename = f"expenses_{date}.txt"
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("No expenses found for this date.")
        return

    item_name = input("Enter item name to search: ").lower()
    results =[]
    for line in lines:
        if item_name in line.lower():
            results.append(line.strip())

    if results:
        print("\n--- Results found---")
        for r in results:
            print(r)
    else:
        print("No matching items found.")

#Searches for an amount inside a date file
def search_by_amount():
    print("\n=== SEARCH BY AMOUNT ===")

    date = input("Enter date (YYYY-MM-DD): ")
    filename = f"expenses_{date}.txt"

    try:
        with open(filename, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("No expenses found for this date.")
        return

    amount = input("Enter amount to search: ")


    if not amount.replace('.', '', 1).isdigit():
        print("Invalid amount! Must be a number.")
        return

    results = []
    for line in lines:
        if amount in line:
            results.append(line.strip())

    if results:
        print("\n--- Results Found ---")
        for r in results:
            print(r)
    else:
        print("No expenses found matching that amount.")


# shows the main menu of the program 
def main_menu():
    print('\n===PERSONAL EXPENSES TRACKER===')
    print("1. Check remaining Balance")
    print("2. View Expenses")
    print("3. Add New Expense")
    print("4. Exit")

    choice = input("Enter your choice(1-4):")
    return choice

#Main loop for the program
def main():
    while True:
        choice = main_menu()
        if choice == "1":
            check_balance()
        

        elif choice == "2":
            while True:
                option =view_expenses_menu()
                if option == "1":
                    search_by_item()
                elif option == "2":
                    search_by_amount()
                elif option == "3":
                    break
                else:
                    print("Invalid choice. Enter 1-3.")

                     
        elif choice == "3":
             add_expense()

        elif choice == "4":
             print("Goodbye! Exiting the program ...")
             break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
main()                       
        

