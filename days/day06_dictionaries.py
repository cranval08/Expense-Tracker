# Day 6: Dictionaries
# Goal: represent each expense as a dict, then group totals by category.

# ---------- 1. One expense as a dictionary ----------
expense = {
    "date": "2026-10-01",
    "category": "food",
    "description": "groceries",
    "amount": 42.50,
}

print("Description: ", expense["description"])
print("Notes: ", expense.get("notes", "no notes")) # safe lookup

expense["amount"] = 45.00       # change a value
expense["payment"] = "card"     # add a new key
print(expense)
print()

# ---------- 2. A list of expense dictionaries ----------
expenses = [
    {"date": "2026-10-01", "category": "Food", "description": "Groceries", "amount": 45.00, "payment": "Cash"},
    {"date": "2026-10-02", "category": "Transport", "description": "Bus pass", "amount": 20.00, "payment": "Cash"},
    {"date": "2026-10-03", "category": "Food", "description": "Lunch", "amount": 12.75, "payment": "Card"},
    {"date": "2026-10-05", "category": "Entertainment", "description": "Movie", "amount": 15.00, "payment": "Card"},
    {"date": "2026-10-06", "category": "Transport", "description": "Taxi", "amount": 18.50, "payment": "Cash"},
    {"date": "2026-10-08", "category": "Food", "description": "Dinner out", "amount": 32.40, "payment": "Card"},
]

# ---------- 3. Loop and print a neat table ----------
print(f"{'Date':<12}{'Category':<15}{'Amount':>8}")
print("-" * 35)
for e in expenses:
    print(f"{e['date']:<12}{e['category']:<15}{e['amount']:>8.2f}")
print()

# ---------- 4. Group totals by category ----------
totals = {}   # starts empty, we fill it as we go

for e in expenses:
    if e["amount"] < 15.00:
        continue
    category = e["category"]
    if category in totals:
        totals[category] += e["amount"]   # seen before: add to it
    else:
        totals[category] = e["amount"]    # first time: create it


print("Totals by category:")
for category, total in totals.items():
    print(f" {category:<15}{total:>8.2f}")

print()
counts = {}
for e in expenses:
    category = e["category"]
    if category in counts:
        counts[category] += 1
    else:
        counts[category] = 1

print("Category count: ")
for category, total in counts.items():
    print(f" {category:<15}{total:>8}")

# ---------- 5. Grand total and biggest category ----------
grand_total = sum(totals.values())
biggest = max(totals, key=totals.get)

print()
print("Category percentage:")
for category, total in totals.items():
    print(f" {category:<15}{(total/grand_total)*100:>8.2f}%")

print()
print(f"Grand total: {grand_total:.2f}")
print(f"Biggest category: {biggest} ({totals[biggest]:.2f})")

