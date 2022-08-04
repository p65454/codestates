"""
Part 1

Chinook 데이터베이스를 이용하여 각 질문에서 명시한 요구사항을 충족하는 SQL 문을 작성합니다.
"""

QUERY_1 = "SELECT Customerid, UPPER(City)||' '||UPPER(Country) AS CityCountry FROM customers"

QUERY_2 = "SELECT LOWER(SUBSTRING(FirstName,1,4)) || LOWER(SUBSTRING(LastName,1,2)) AS Nickname FROM customers"

QUERY_3 = "SELECT EmployeeId FROM employees WHERE (DATE('2020-01-01') - HireDate) > 7 ORDER BY LastName"

QUERY_4 = """\
SELECT FirstName || LastName || InvoiceId AS OrderNo
FROM invoices JOIN customers ON customers.CustomerId = invoices.CustomerId
ORDER BY FirstName, LastName, InvoiceId;"""

QUERY_5 = """ SELECT Name From tracks 
WHERE AlbumId IN (
	SELECT AlbumId FROM albums
	WHERE Title LIKE 'Unplugged' OR Title LIKE 'Outbreak'
);
"""
