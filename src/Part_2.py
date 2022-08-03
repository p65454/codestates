"""
Part 2

Chinook.db를 이용하여 각 질문에서 명시한 요구사항을 충족하는 SQL 문을 작성합니다. 데이터베이스 엔진은 SQLite를 사용합니다.
"""

QUERY_1 = """SELECT Title
FROM
albums
WHERE AlbumId = 31;"""

QUERY_2 = """SELECT AlbumId 
FROM albums AS al
JOIN artists AS art
ON al.ArtistId = art.ArtistId 
WHERE art.Name
LIKE '%the%';"""

QUERY_3 =  """SELECT InvoiceId
FROM invoices
WHERE BillingCity 
IN ('Stuttgart', 'Oslo', 'Redmond')
ORDER BY InvoiceId;"""

QUERY_4 = """SELECT trackId
FROM tracks
WHERE Name
LIKE 'The%';"""

QUERY_5 = """SELECT CustomerId 
FROM customers AS cus
WHERE Email
LIKE '%gmail.com';"""

QUERY_6 = """SELECT InvoiceId
FROM invoices
WHERE CustomerId IN (29, 30, 63) AND Total BETWEEN 1 AND 3;"""

QUERY_7 = "SQL 쿼리문을 작성해 주세요."

QUERY_8 = "SQL 쿼리문을 작성해 주세요."

QUERY_9 = "SQL 쿼리문을 작성해 주세요."

QUERY_10 = "SQL 쿼리문을 작성해 주세요."
