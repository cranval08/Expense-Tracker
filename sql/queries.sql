-- Day 21: save your 10 favorite queries here, each with a comment.

-- 1. Five biggest expenses
SELECT * FROM expenses ORDER BY amount DESC LIMIT 5;

-- 2. Total spent per category
SELECT category, SUM(amount) AS total
FROM expenses
GROUP BY category
ORDER BY total DESC;

-- 3. TODO: this month's spending

-- 4. TODO: average expense per category

-- 5. TODO: number of expenses per category

-- 6-10. TODO: add your own
