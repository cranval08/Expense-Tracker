# reports.py: totals and printing


def total_amount(expenses):
    """Add up the amount of every expense."""
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
            totals[category] += e["amount"]
        else:
            totals[category] = e["amount"]
    return totals


def format_expense(e):
    """Return one expense as a table row (a string)."""
    return f"{e['date']:<12}{e['category']:<15}{e['description']:<18}{e['amount']:>8.2f}"


def print_expenses(expenses):
    """Print the full table with a total."""
    if len(expenses) == 0:
        print("No expenses yet.")
        return

    print(f"{'Date':<12}{'Category':<15}{'Description':<18}{'Amount':>8}")
    print("-" * 53)
    for e in expenses:
        print(format_expense(e))
    print("-" * 53)
    print(f"{'Total':<45}{total_amount(expenses):>8.2f}")


def print_category_totals(expenses):
    """Print the total for each category."""
    if len(expenses) == 0:
        print("No expenses yet.")
        return
    for category, total in totals_by_category(expenses).items():
        print(f"  {category:<15}{total:>8.2f}")


def print_biggest(expenses):
    if len(expenses) == 0:
        print("No expenses yet.")
        return

    biggest = expenses[0]

    for e in expenses:
        if e["amount"] > biggest["amount"]:
            biggest = e

    print(biggest)