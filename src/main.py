# main.py: the menu. Run this file.
from models import make_expense
from reports import print_expenses, print_category_totals, print_biggest
from storage import load_expenses, append_expense, load_sample


def main():
    expenses = load_expenses()
    print("=== Expense Tracker v0.2 ===")
    print(f"Loaded {len(expenses)} saved expenses.")

    while True:
        print()
        print("1) Add expense")
        print("2) List expenses")
        print("3) Totals by category")
        print("4) Biggest expense")
        print("5) Quit")
        choice = input("Choose 1-5: ").strip()

        if choice == "1":
            date = input("Date (YYYY-MM-DD): ").strip()
            category = input("Category: ")
            description = input("Description: ")
            amount_text = input("Amount: ").strip()

            expense = make_expense(date, category, description, amount_text)
            if expense is None:
                print("Amount must be a positive number or category is required or follow date format correctly. Expense not saved.")
            else:
                expenses.append(expense)
                append_expense(expense)
                print("Saved!")

        elif choice == "2":
            is_sample = input("Load sample data? (Y/N): ").strip().capitalize()
            if is_sample == "N":
                print()
                print_expenses(expenses)
            elif is_sample == "Y":
                expenses = load_sample()
                print()
                print_expenses(expenses)

        elif choice == "3":
            is_sample = input("Print sample data totals by category? (Y/N): ").strip().capitalize()
            if is_sample == "N":
                print()
                print_category_totals(expenses)
            elif is_sample == "Y":
                expenses = load_sample()
                print()
                print_category_totals(expenses)
            

        elif choice == "4":
            print()
            print_biggest(expenses)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Please enter 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()