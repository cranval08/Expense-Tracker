-- Day 15: create the expenses table
-- Run with:  sqlite3 data/expenses.db < sql/schema.sql

CREATE TABLE IF NOT EXISTS expenses (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    amount      REAL    NOT NULL CHECK (amount > 0),
    category    TEXT    NOT NULL,
    description TEXT,
    date        TEXT    NOT NULL   -- format: YYYY-MM-DD
);

-- Day 19: uncomment to add a categories table and link it.
-- (Hint: you will need to migrate the existing category text values.)
--
-- CREATE TABLE IF NOT EXISTS categories (
--     id   INTEGER PRIMARY KEY AUTOINCREMENT,
--     name TEXT NOT NULL UNIQUE
-- );
--
-- ALTER TABLE expenses ADD COLUMN category_id INTEGER REFERENCES categories(id);
