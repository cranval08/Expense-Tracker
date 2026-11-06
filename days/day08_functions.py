# Day 8: Functions
# Goal: turn repeated Week 1 logic into small reusable functions.

# ---------- 1. Simple functions ----------
def greet(name):
    print(f"Hello, {name}!")          # prints, returns nothing

def add_tax(amount, rate=0.10):
    return amount * (1 + rate)        # returns a value


greet("Sam")
print(f"With default tax: {add_tax(100):.2f}")
print(f"With 20% tax:     {add_tax(100, 0.2):.2f}")
print()



# ---------- 2. Expense functions ----------
def is_valid_amount(text):
    """Return True if text is a positive number like 12 or 12.50."""
    return text.replace(".", "", 1).isdigit()

def total_amount(expenses):
    """Add up the amount of every expense in the list."""
    total = 0
    for e in expenses:
        total += e["amount"]
    return total

def totals_by_category(expenses):
    """Return a dict like {'Food': 57.75, 'Transport': 20.0}."""
    totals = {}
    for e in expenses:
        category = e["category"]
        if category in totals:
            totals[category] += e ["amount"]
        else:
            totals[category] = e["amount"]
    return totals

def format_expense(e):
    """Return one expense as a neat table row (a string)."""
    return f"{e['date']:<12}{e['category']:<15}{e['description']:<18}{e['amount']:>8.2f}"

def print_expenses(expenses):
    """Print the full table with a total."""
    if len(expenses) == 0:
        print("No expenses yet.")
        return                          # leave the function early

    print(f"{'Date':<12}{'Category':<15}{'Description':<18}{'Amount':>8}")
    print("-" * 53)
    for e in expenses:
        print(format_expense(e))
    print("-" * 53)
    print(f"{'Total':<45}{total_amount(expenses):>8.2f}")

def average_amount(expenses):
    return total_amount(expenses) / len(expenses)

def biggest_expense(expenses):
    if len(expenses) == 0:
        print("No expenses yet.")
        return

    biggest = expenses[0]

    for e in expenses:
        if e["amount"] > biggest["amount"]:
            biggest = e

    return biggest

def filter_by_category(expenses, category):
    matching = []
          
    for e in expenses:
        if e["category"] == category:
            matching.append(e)

    if len(matching) == 0:
        print("Category not found.")
        return

    print_expenses(matching)

def make_expense(date, category, description, amount_text):
    fixedDate = date.strip().title()
    fixedCategory = category.strip().title()
    fixedDescription = description.strip().title()

    if type(amount_text) != int:
        if is_valid_amount(amount_text):
            fixedAmountText = float(amount_text)
        else:
            print("Enter a valid positive number.")
    else:
        fixedAmountText = float(amount_text)

    if fixedDate and fixedCategory and fixedDescription:
        isValid = True
    else:
        print("Expense is invalid (Empty arguments).")
        return None

    if isValid:
        expenses.append({"date": fixedDate, "category": fixedCategory, "description": fixedDescription, "amount": fixedAmountText})

    return expenses

# ---------- 3. Using them ----------
expenses = [
    {"date": "2026-10-01", "category": "Food", "description": "Groceries", "amount": 45.00},
    {"date": "2026-10-02", "category": "Transport", "description": "Bus pass", "amount": 20.00},
    {"date": "2026-10-03", "category": "Food", "description": "Lunch", "amount": 12.75},
    {"date": "2026-10-05", "category": "Entertainment", "description": "Movie", "amount": 15.00},
]

print_expenses(expenses)
print()

print("Totals by category:")
for category, total in totals_by_category(expenses).items():
    print(f"  {category:<15}{total:8.2f}")
print()


# Testing the validator
for text in ["12.50", "7", "abc", "-5", "1.2.3"]:
    print(f"is_valid_amount({text!r})) -> {is_valid_amount(text)}")
print()

# Average
print(f"Average expense: {average_amount(expenses):.2f}")
print()

# Biggest
print(f"Biggest expense: {biggest_expense(expenses)['description']} ({biggest_expense(expenses)['amount']}) ")
print()

# Filter by category
filter_by_category(expenses, "Entertainment")
print()

# Make expense
print(f"{make_expense("2027-01-01", "Transport", "Train ticket", 30)}")