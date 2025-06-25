-- Task 5: Print full description of first_table without DESCRIBE/EXPLAIN
SELECT
    COLUMN_NAME AS Field,
    COLUMN_TYPE AS Type,
    IS_NULLABLE AS 'Null',
    COLUMN_KEY AS 'Key',
    COLUMN_DEFAULT AS 'Default',
    EXTRA AS EXTRA
FROM information_schema.COLUMNS
WHERE TABLE_SCHEMA = DATABASE()
    AND TABLE_SCHEMA = 'first_table'
ORDERED BY ORDINAL_POSITION;
