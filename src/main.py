# Day 7: Expense Tracker v0.1
# Everything from Week 1 in one program: input, if/elif, lists, dicts, loops.

expenses = [
    {"date": "2026-10-01", "category": "Food", "description": "Groceries", "amount": 45.00},
    {"date": "2026-10-02", "category": "Transport", "description": "Bus pass", "amount": 20.00},
    {"date": "2026-10-05", "category": "Entertainment", "description": "Movie", "amount": 15.00},
]

print("=== Expense Tracker v0.1 ===")

while True:
    print()
    print("1) Add expense")
    print("2) List expenses")
    print("3) Totals by category")
    print("4) Show biggest expense")
    print("5) Quit")
    choice = input("Choose 1-5: ").strip()

    if choice == "1":
        date = input("Date (YYYY-MM-DD): ").strip()
        category = input("Category: ").strip().title()
        description = input("Description: ").strip()
        amount_text = input("Amount: ").strip()

        # allow digits with at most one decimal point
        if not amount_text.replace(".", "", 1).isdigit():
            print("Amount must be a positive number. Expense not saved.")
        elif category == "":
            print("Category must not be empty. Expense not saved.")
        else:
            expenses.append({
                "date": date,
                "category": category,
                "description": description,
                "amount": float(amount_text)
            })
            print("Saved!")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses yet.")
        else:
            choose = input("Search by category? (Y/N): ").strip().capitalize()
            if choose == "N":
                print()
                print(f"{'Date':<12}{'Category':<15}{'Description':<18}{'Amount':>8}")
                print("-" * 53)
                total = 0
                for e in expenses:
                    print(f"{e['date']:<12}{e['category']:<15}{e['description']:<18}{e['amount']:>8.2f}")
                    total += e["amount"]
                print("-" * 53)
                print(f"{'Total':<45}{total:>8.2f}")
            elif choose == "Y":
                search = input("Category name: ").strip().capitalize()
                total = 0

                count = []
                for e in expenses:
                    count.append(e["category"])
                if search not in count:
                    print("Category not found.")
                else: 
                    print()
                    print(f"{'Date':<12}{'Category':<15}{'Description':<18}{'Amount':>8}")
                    print("-" * 53)
                    for e in expenses:
                        if e["category"] != search:
                            continue
                        print(f"{e['date']:<12}{e['category']:<15}{e['description']:<18}{e['amount']:>8.2f}")
                        total += e["amount"]
                    print("-" * 53)
                    print(f"{'Total':<45}{total:>8.2f}")
            else:
                print("Input must be 'Y' or 'N'.")

    elif choice =="3":
        totals = {}
        for e in expenses:
            category = e["category"]
            if category in totals:
                totals[category] += e["amount"]
            else:
                totals[category] = e["amount"]

        grand_total = sum(totals.values())

        print()
        for category, total in totals.items():
            print(f" {category:<15}{total:>8.2f}{(total / grand_total) * 100:>10}%")
        print("-" * 35)
        print(f" {grand_total:>23.2f}{'100%':>10}")

    elif choice == "4":
        counts = {}
        for e in expenses:
            category = e["category"]
            if category in counts:
                counts[category] += e["amount"]
            else:
                counts[category] = e["amount"]
        biggest = max(counts, key=counts.get)
        print(f"Biggest expense: {biggest} (${counts[biggest]})")


    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Please enter 1, 2, 3, or 4")