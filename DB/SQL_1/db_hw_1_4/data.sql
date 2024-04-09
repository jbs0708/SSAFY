SELECT
    *
FROM
    tracks
WHERE
    name LIKE '%love%';


SELECT
    *
FROM
    tracks
WHERE
    GenreId = 1
    AND Milliseconds >= 300000
ORDER BY
    UnitPrice;


SELECT
    GenreId, COUNT(*) AS 'TotalTracks'
FROM
    tracks
GROUP BY
    GenreId;


SELECT
    GenreId, SUM(UnitPrice) AS TotalPrice
FROM
    tracks
GROUP BY
    GenreId
HAVING
    TotalPrice >= 100;