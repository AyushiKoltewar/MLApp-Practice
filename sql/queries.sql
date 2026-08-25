-- MLApp: Analytical queries

-- Total revenue per customer
SELECT
    customer_id,
    SUM(amount) AS total_spend,
    COUNT(*) AS transaction_count
FROM transactions
GROUP BY customer_id
ORDER BY total_spend DESC;

-- MLAPP-1234: Customer segment counts
SELECT segment, COUNT(*) AS customer_count
FROM customer_segments
GROUP BY segment
ORDER BY customer_count DESC;