-- @block Show all book in order they appear in the Bible
SELECT book
FROM versiculos
GROUP BY book
ORDER BY MIN(id);

-- @block Count chapters and verses in each book
SELECT book,
    COUNT(DISTINCT(chapter)) as chapter_count,
    COUNT(*) as verse_count
FROM versiculos
GROUP BY book
ORDER BY MIN(id);

-- @block Count verses in each chapter of each book
SELECT book,
    chapter,
    COUNT(verse) AS verse_count
FROM versiculos
GROUP BY book,
    chapter
ORDER BY MIN(id);

-- @block Count total verses in the Bible
SELECT COUNT(*) AS total_verses
FROM versiculos;

-- @block Count average characters per
SELECT book, chapter, AVG(LENGTH(text))
FROM versiculos
GROUP BY book, chapter

-- @block Count average characters per
SELECT AVG(LENGTH(text))
FROM versiculos

-- @block Percentiles of verse text length
WITH lengths AS (
    SELECT LENGTH(TRIM(text)) AS len
    FROM versiculos
    WHERE text IS NOT NULL
),
r AS (
    SELECT
        len,
        ROW_NUMBER() OVER (ORDER BY len) AS rn,
        COUNT(*) OVER () AS cnt
    FROM lengths
)
SELECT
    MIN(CASE WHEN rn = CAST(0.0 * (cnt - 1) + 1 AS INT) THEN len END) AS p0,
    MIN(CASE WHEN rn = CAST(0.1 * (cnt - 1) + 1 AS INT) THEN len END) AS p10,
    MIN(CASE WHEN rn = CAST(0.25 * (cnt - 1) + 1 AS INT) THEN len END) AS p25,
    MIN(CASE WHEN rn = CAST(0.5 * (cnt - 1) + 1 AS INT) THEN len END) AS p50,
    MIN(CASE WHEN rn = CAST(0.75 * (cnt - 1) + 1 AS INT) THEN len END) AS p75,
    MIN(CASE WHEN rn = CAST(0.9 * (cnt - 1) + 1 AS INT) THEN len END) AS p90,
    MIN(CASE WHEN rn = CAST(0.95 * (cnt - 1) + 1 AS INT) THEN len END) AS p95,
    MIN(CASE WHEN rn = CAST(0.99 * (cnt - 1) + 1 AS INT) THEN len END) AS p99,
    MIN(CASE WHEN rn = CAST(1.0 * (cnt - 1) + 1 AS INT) THEN len END) AS p100
FROM r;

-- @block Check for duplicate verses (same book, chapter, verse)
SELECT book,
    chapter,
    verse,
    COUNT(*) as count
FROM versiculos
GROUP BY book,
    chapter,
    verse
HAVING count > 1;

-- @block Check for missing verse numbers in each chapter
SELECT book,
    chapter,
    MIN(verse) as first_verse,
    MAX(verse) as last_verse
FROM versiculos
GROUP BY book,
    chapter;

-- To check for missing verses, you may need to export the verse numbers and compare with a sequence in your analysis tool.
-- @block Check for NULLs in required fields
SELECT *
FROM versiculos
WHERE book IS NULL
    OR chapter IS NULL
    OR verse IS NULL
    OR text IS NULL;

-- @block Check for negative or zero chapter/verse numbers
SELECT *
FROM versiculos
WHERE chapter <= 0
    OR verse <= 0;
