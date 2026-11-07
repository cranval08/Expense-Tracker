# models.py: what an expense looks like, and whether it's valid

FIELDS = ["date", "category", "description", "amount"]


def is_valid_amount(text):
    """Return True if text is a positive number like 12 or 12.50."""
    return text.replace(".", "", 1).isdigit()

def is_valid_date(text):
    """Return True if text is 10 characters long with - at positions 4 and 7"""
    return (len(text) == 10 and text[4] == "-" and text[7] == '-')

def make_expense(date, category, description, amount_text):
    """Return an expense dict, or None if the amount or category is invalid."""
    if not is_valid_amount(amount_text) or not is_valid_date(date):
        return None

    cleaned_category = category.strip()
    if not cleaned_category:
        return None
    
    return {
        "date": date,
        "category": category.strip().title(),
        "description": description.strip(),
        "amount": float(amount_text),
    }

