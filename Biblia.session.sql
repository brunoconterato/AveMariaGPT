-- @block Show all books in the order in which they appear in the Bible
SELECT book
FROM versiculos
GROUP BY book
ORDER BY MIN(pdf_page);

-- @block Count chapters and logical verses in each book
SELECT
    book,
    COUNT(DISTINCT chapter) AS chapter_count,
    SUM(verse_end - verse_start + 1) AS verse_count
FROM versiculos
GROUP BY book
ORDER BY MIN(pdf_page);

-- @block Count chapters and logical verses in each book chapter
SELECT
    book,
    chapter,
    SUM(verse_end - verse_start + 1) AS verse_count
FROM versiculos
GROUP BY book, chapter
ORDER BY MIN(pdf_page);

-- @block Count logical verses in the Bible
SELECT SUM(verse_end - verse_start + 1) AS total_verses
FROM versiculos;

-- @block Count average characters per book and chapter
SELECT
    book,
    chapter,
    AVG(LENGTH(text)) AS average_characters
FROM versiculos
GROUP BY book, chapter
ORDER BY MIN(pdf_page);

-- @block Count average characters per verse block
SELECT AVG(LENGTH(text)) AS average_characters
FROM versiculos;

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

-- @block Check for duplicate verse blocks
SELECT
    book,
    chapter,
    verse_start,
    verse_end,
    COUNT(*) AS count
FROM versiculos
GROUP BY book, chapter, verse_start, verse_end
HAVING count > 1;

-- @block Check the verse range covered by each chapter
SELECT
    book,
    chapter,
    MIN(verse_start) AS first_verse,
    MAX(verse_end) AS last_verse,
    SUM(verse_end - verse_start + 1) AS covered_verses
FROM versiculos
GROUP BY book, chapter
ORDER BY MIN(pdf_page);

-- A complete gap check requires comparing these ranges with an expected sequence.
-- @block Check NULLs in fields required by Verse
SELECT *
FROM versiculos
WHERE book IS NULL
    OR chapter IS NULL
    OR text IS NULL
    OR pdf_page IS NULL
    OR need_review IS NULL
    OR raw_verse_marker IS NULL;

-- @block Check invalid chapter and verse ranges
SELECT *
FROM versiculos
WHERE chapter <= 0
    OR verse_start <= 0
    OR verse_end <= 0
    OR verse_start > verse_end;

-- @block Check parse issues marked for review
SELECT *
FROM versiculos
WHERE need_review = 1
    OR parse_issue IS NOT NULL;
