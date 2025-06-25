-- Task 16: List score and name for rows where name is not empty, ordered by score desc
SELECT
    score,
    name
FROM second_table
WHERE name is not NULL
    AND name <> ''
ORDER BY score DESC;
