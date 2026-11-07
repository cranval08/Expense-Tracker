# storage.py: saving and loading expenses as CSV
import csv
from pathlib import Path

from models import FIELDS

# src/storage.py -> parent is src/, parent.parent is the project root
DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "expenses.csv"
SAMPLE_FILE = Path(__file__).resolve().parent.parent / "data" / "sample_expenses.csv"


def load_expenses(path=DATA_FILE):
    """Read a CSV into a list of expense dicts. Skips rows with a bad amount."""
    expenses = []
    skipped = 0
    try:
        with open(path, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    row["amount"] = float(row["amount"])
                except (ValueError, TypeError):
                    skipped += 1
                    continue
                expenses.append(row)
    except FileNotFoundError:
        pass    # first run: no file yet, so start empty

    if skipped > 0:
        print(f"(Skipped {skipped} row(s) with a bad amount.)")
    return expenses


def append_expense(expense, path=DATA_FILE):
    """Add one expense to the end of the CSV. Write the header only for a new file."""
    path = Path(path)
    path.parent.mkdir(exist_ok=True)
    is_new_file = not path.exists()
    with open(path, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        if is_new_file:
            writer.writeheader()
        writer.writerow(expense)

def load_sample(path=SAMPLE_FILE):
    expenses = []
    skipped = 0
    try:
        with open(path, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    row["amount"] = float(row["amount"])
                except (ValueError, TypeError):
                    skipped += 1
                    continue
                expenses.append(row)
    except FileNotFoundError:
        pass    # first run: no file yet, so start empty

    if skipped > 0:
        print(f"(Skipped {skipped} row(s) with a bad amount.)")
    return expenses