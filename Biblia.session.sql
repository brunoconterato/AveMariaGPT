-- @block Show all book in order they appear in the Bible
SELECT book
FROM versiculos
GROUP BY book
ORDER BY MIN(id);

-- @block Count chapters in each book
SELECT book,
    COUNT(DISTINCT(chapter)) as chapter_count
FROM versiculos
GROUP BY book
ORDER BY MIN(id);

-- @block Count verses in each chapter of each book
SELECT book,
    chapter,
    COUNT(verse) AS verse_count
FROM versiculos
GROUP BY book, chapter
ORDER BY MIN(id);

-- @block Count total verses in the Bible
SELECT COUNT(*) AS total_verses
FROM versiculos;