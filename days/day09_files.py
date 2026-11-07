# Day 9: Reading and writing files
# Goal: save expenses to a CSV file and load them back.

# -- Learn -- #
with open("notes.txt", "w") as f:    # "w" = write (replaces the file)
    f.write("hello\n")

with open("notes.txt", "r") as f:    # "r" = read
    text = f.read()

# -- Main -- #
import csv
from pathlib import Path

# Find the project's data folder, no matter where you run the program from.
# This assumes this file is inside a folder (like days/) one level below the
# project root. If it sits directly in the root, change .parent.parent to .parent
DATA_DIR = Path(__file__).resolve().parent.parent / "data"
DATA_DIR.mkdir(exist_ok=True)

FIELDS = ["date", "category", "description", "amount"]


# ---------- 1. Plain text: write, append, read ----------
notes_file = DATA_DIR / "day09_notes.txt"

with open(notes_file, "w") as f:
    f.write("First line\n")
    f.write("Second line\n")

with open(notes_file, "a") as f:
    f.write("Third line (appended)\n")

with open(notes_file, "r") as f:
    for line in f:
        print(line.strip())
print()


# ---------- 2. Save expenses to CSV ----------
def save_expenses(expenses, path):
    """Write a list of expense dicts to a CSV file."""
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(expenses)


# ---------- 3. Load expenses to CSV ----------
def load_expenses(path):
    """Read a CSV file into a list of expense dicts. Missing file -> empty list."""
    expenses = []
    try:
        with open(path, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["amount"] = float(row["amount"])   # text -> number
                expenses.append(row)
    except FileNotFoundError:
        print(f"(No file at {path} yet, starting empty.)")
    return expenses

# ---------- 4. Try it out ----------
my_file = DATA_DIR / "my_expenses_test.csv"

expenses = load_expenses(my_file)          # first run: file doesn't exist yet
print(f"Loaded {len(expenses)} expenses")

expenses.append(
    {"date": "2026-11-09", "category": "Food", "description": "Coffee", "amount": 4.50}
)

save_expenses(expenses, my_file)
print(f"Saved. The file now has {len(expenses)} expenses")
print()

# ---------- 5. Load the real sample data ----------
sample = load_expenses(DATA_DIR / "sample_expenses.csv")
print(f"Sample file: {len(sample)} expenses")
print(f"Sample total: {sum(e['amount'] for e in sample):.2f}")
if sample:
    print("First one:", sample[0])
print()


# ----- Count Lines ----- 
def count_lines(path):
    count = 0
    with open(path, "r") as f:
        for line in f:
            count += 1

    return count

print(f"Lines total: {count_lines(notes_file)}")


# ----- Totals by Category -----
def totals_by_category(path):
    expenses = load_expenses(path)
    totals = {}
    for e in expenses:
        category = e["category"]
        if category in totals:
            totals[category] += e ["amount"]
        else:
            totals[category] = e["amount"]

    return totals

data_sample = DATA_DIR / "sample_expenses.csv"
print(totals_by_category(data_sample))


# ----- Append Expense -----
def append_expenses(expense, path):
    is_new_file = not Path(path).exists()          # check BEFORE opening
    with open(path, "a", newline="") as f:         # "a" = add to the end
        writer = csv.DictWriter(f, fieldnames = FIELDS)
        if is_new_file:
            writer.writeheader()
        writer.writerow(expense)                   # writerow (singular) = one row

new_data_sample = DATA_DIR / "append_expense.csv"
if new_data_sample.exists():
    new_data_sample.unlink()       # delete the file so each run starts fresh

new_expense = {"date": "2026-06-07", "category": "Food", "amount": 12.50}
append_expenses(new_expense, new_data_sample)


# ----- Skip bad rows -----
def load_good_expenses(path):
    expenses = []
    skipped = 0
    try:
        with open(path, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    row["amount"] = float(row["amount"])
                except (ValueError, TypeError):    # "abc", "" or a missing value
                    skipped += 1
                    continue                       # skip this row, go to the next
                expenses.append(row)
    except FileNotFoundError:
        print(f"(No file at {path} yet, starting empty.)")

    if skipped > 0:
        print(f"(Skipped {skipped} row(s) with a bad amount.)")
    return expenses

messy = DATA_DIR / "messy_test.csv"
with open(messy, "w", newline="") as f:
    f.write("date,category,description,amount\n")
    f.write("2026-11-01,Food,Lunch,12.50\n")
    f.write("2026-11-02,Food,Dinner,abc\n")
    f.write("2026-11-03,Transport,Taxi,\n")
    f.write("2026-11-04,Transport,Bus,2.00\n")

good = load_good_expenses(messy)
print("Good rows:", len(good))