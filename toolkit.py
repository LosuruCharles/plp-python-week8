# toolkit.py
# Personal Mini-Toolkit
# A menu-driven program with four tools:
#   1. To-Do List   2. Calculator   3. Number Guessing Game   4. Expense Tracker

import random


# DATA THAT CHANGES WHILE THE PROGRAM RUNS (stored in lists)

todo_list = []          # tasks for the To-Do List
expense_names = []      # what each expense was for
expense_amounts = []    # how much each expense cost (same position as name)


# WELCOME MESSAGE

print("Welcome to your Personal Mini-Toolkit!")


# MAIN MENU LOOP - keeps running until the user chooses Quit

running = True
while running:
    print()
    print("==============================")
    print("   PERSONAL MINI-TOOLKIT")
    print("==============================")
    print("  1. To-Do List")
    print("  2. Calculator")
    print("  3. Number Guessing Game")
    print("  4. Expense Tracker")
    print("  5. Quit")
    print("==============================")
    choice = input("Enter your choice (1-5): ").strip()

   
    # TOOL 1: TO-DO LIST
  
    if choice == "1":
        print("\n--- To-Do List ---")
        in_todo = True
        while in_todo:
            print("\n  1. Add a task")
            print("  2. View tasks")
            print("  3. Remove a task")
            print("  4. Back to main menu")
            todo_choice = input("Choose an option (1-4): ").strip()

            if todo_choice == "1":
                task = input("Enter the new task: ").strip()
                if task == "":
                    print("A task can't be empty. Nothing was added.")
                else:
                    todo_list.append(task)
                    print(f"Added: {task}")

            elif todo_choice == "2":
                if len(todo_list) == 0:
                    print("Your to-do list is empty. Nice and clear!")
                else:
                    print("\nYour tasks:")
                    number = 1
                    for task in todo_list:
                        print(f"  {number}. {task}")
                        number = number + 1

            elif todo_choice == "3":
                if len(todo_list) == 0:
                    print("There is nothing to remove - the list is empty.")
                else:
                    number = 1
                    for task in todo_list:
                        print(f"  {number}. {task}")
                        number = number + 1
                    remove_text = input("Number of the task to remove: ").strip()
                    if remove_text.isdigit() and 1 <= int(remove_text) <= len(todo_list):
                        removed = todo_list.pop(int(remove_text) - 1)
                        print(f"Removed: {removed}")
                    else:
                        print("That's not a valid task number.")

            elif todo_choice == "4":
                in_todo = False

            else:
                print("Please enter a number from 1 to 4.")

   
    # TOOL 2: CALCULATOR
   
    elif choice == "2":
        print("\n--- Calculator ---")
        print("Type 'back' at any time to return to the main menu.")
        in_calc = True
        while in_calc:
            first_text = input("\nFirst number: ").strip()
            if first_text.lower() == "back":
                in_calc = False
            else:
                operator = input("Operator (+, -, *, /): ").strip()
                second_text = input("Second number: ").strip()

                # try/except stops the program crashing if the text isn't a number
                try:
                    first = float(first_text)
                    second = float(second_text)
                    valid_numbers = True
                except ValueError:
                    valid_numbers = False

                if not valid_numbers:
                    print("Please enter real numbers (like 4 or 3.5).")
                elif operator == "+":
                    print(f"{first} + {second} = {first + second}")
                elif operator == "-":
                    print(f"{first} - {second} = {first - second}")
                elif operator == "*":
                    print(f"{first} * {second} = {first * second}")
                elif operator == "/":
                    if second == 0:
                        print("You can't divide by zero!")
                    else:
                        print(f"{first} / {second} = {first / second}")
                else:
                    print("Unknown operator. Use +, -, * or /.")

    
    # TOOL 3: NUMBER GUESSING GAME
  
    elif choice == "3":
        print("\n--- Number Guessing Game ---")
        secret_number = random.randint(1, 100)
        max_attempts = 7
        guesses = []            # remembers every guess in this round
        won = False
        print("I'm thinking of a number between 1 and 100.")
        print(f"You have {max_attempts} attempts. Good luck!")

        while len(guesses) < max_attempts and not won:
            attempts_left = max_attempts - len(guesses)
            guess_text = input(f"\nAttempt ({attempts_left} left) - your guess: ").strip()

            if not guess_text.isdigit():
                print("Please enter a whole number.")
            elif int(guess_text) < 1 or int(guess_text) > 100:
                print("Stay between 1 and 100, please.")
            else:
                guess = int(guess_text)
                guesses.append(guess)
                if guess == secret_number:
                    won = True
                elif guess < secret_number:
                    print("Too low! Try a higher number.")
                else:
                    print("Too high! Try a lower number.")

        if won:
            print(f"\nCorrect! You got it in {len(guesses)} guesses.")
        else:
            print(f"\nOut of attempts. The number was {secret_number}.")
        print(f"Your guesses were: {guesses}")

   
    # TOOL 4: EXPENSE TRACKER
  
    elif choice == "4":
        print("\n--- Expense Tracker ---")
        in_expenses = True
        while in_expenses:
            print("\n  1. Add an expense")
            print("  2. View expenses and total")
            print("  3. Remove an expense")
            print("  4. Back to main menu")
            exp_choice = input("Choose an option (1-4): ").strip()

            if exp_choice == "1":
                name = input("What was the expense for? ").strip()
                amount_text = input("How much did it cost? ").strip()
                try:
                    amount = float(amount_text)
                    valid_amount = amount >= 0
                except ValueError:
                    valid_amount = False

                if name == "":
                    print("The description can't be empty. Nothing was added.")
                elif not valid_amount:
                    print("The amount must be a number that is 0 or more.")
                else:
                    expense_names.append(name)
                    expense_amounts.append(amount)
                    print(f"Added: {name} - {amount:.2f}")

            elif exp_choice == "2":
                if len(expense_names) == 0:
                    print("No expenses recorded yet.")
                else:
                    print("\nYour expenses:")
                    for i in range(len(expense_names)):
                        print(f"  {i + 1}. {expense_names[i]} - {expense_amounts[i]:.2f}")
                    total_spent = sum(expense_amounts)
                    print(f"Total spent: {total_spent:.2f}")

            elif exp_choice == "3":
                if len(expense_names) == 0:
                    print("There are no expenses to remove.")
                else:
                    for i in range(len(expense_names)):
                        print(f"  {i + 1}. {expense_names[i]} - {expense_amounts[i]:.2f}")
                    remove_text = input("Number of the expense to remove: ").strip()
                    if remove_text.isdigit() and 1 <= int(remove_text) <= len(expense_names):
                        index = int(remove_text) - 1
                        removed_name = expense_names.pop(index)
                        expense_amounts.pop(index)
                        print(f"Removed: {removed_name}")
                    else:
                        print("That's not a valid expense number.")

            elif exp_choice == "4":
                in_expenses = False

            else:
                print("Please enter a number from 1 to 4.")

   
    # QUIT

    elif choice == "5":
        print("\nThanks for using the Mini-Toolkit. Goodbye!")
        running = False


    # ANYTHING ELSE = INVALID CHOICE
   
    else:
        print(f"Sorry, '{choice}' isn't on the menu. Please enter a number from 1 to 5.")