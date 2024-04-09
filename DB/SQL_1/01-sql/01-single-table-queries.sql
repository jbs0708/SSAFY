-- 01. Querying data
SELECT
    LastName
FROM
    employees;


SELECT
    LastName, FirstName
FROM
    employees;


SELECT
    *
FROM
    employees;


SELECT
    FirstName AS '이름'
FROM
    employees;


SELECT
    Name,
    Milliseconds / 60000 AS '재생 시간(분)'
FROM
    tracks;


SELECT
    FirstName
FROM
    employees
ORDER BY
    FirstName;


SELECT
    FirstName
FROM
    employees
ORDER BY
    FirstName DESC;


SELECT DISTINCT
    Country
FROM
    customers
ORDER BY
    Country;


SELECT
    LastName, FirstName, City
FROM
    customers
WHERE
    City = 'Prague';


SELECT
    LastName, FirstName, City
FROM
    customers
WHERE
    City != 'Prague';


SELECT
    LastName, FirstName, Company, Country
FROM
    customers
WHERE
    Company IS NULL
    AND Country = 'USA';


SELECT
    Name, Bytes
FROM
    tracks
WHERE
    Bytes BETWEEN 100000 and 500000
    -- Bytes >= 100000
    -- AND Bytes <= 500000;
ORDER BY
    Bytes;


SELECT
    LastName, FirstName, Country
FROM
    customers
WHERE
    Country NOT IN ('Canada', 'Germany', 'France');


SELECT
    LastName, FirstName, Country
FROM
    customers
WHERE
    LastName LIKE '%son';


SELECT
    LastName, FirstName
FROM
    customers
WHERE
    FirstName LIKE '___a';






-- 02. Sorting data

-- NULL 정렬 예시

-- 03. Filtering data

-- 04. Grouping data

