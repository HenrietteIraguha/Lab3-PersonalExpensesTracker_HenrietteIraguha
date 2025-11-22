PERSONAL EXPENSES TRACKER

This project is a  **command-line application**
designed to help users track daily expenses, view past spending, and
keep track of  their remaining balance.


# main features 

 1. Add new expenses 
 2. check remaining balance 
 3. view expenses
 4. search expenses by amount or by  item name 
 5. Automate file storage
 6. Archives files according to the date 

# Files

1. expenses-tracker.py (main Program file) 
2. balance.txt (Stores current balance)
3. archive_expenses.sh (Script to archive old expense files)

# How the Program Works
Run:
expenses-tracker.py file 

## 2. Main Menu Options

    1. Check remaining Balance
    2. View Expenses
    3. Add New Expense
    4. Exit

and then follow the prompts 

## 3. Archiving 
Run:

./archive_expenses.sh
The script Creates an archives/ folder if there is  none and moves the chosen expense file and then  Logs the action in archive_log.txt
