-- Task 11: List score and name for rows with score >= 10, ordered by score descending
SELECT
    score,
    name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
