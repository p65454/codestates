"""
Part 3

STORE.db를 이용하여 각 이미지로 전달된 결과가 출력될 수 있는 SQL 문을 작성합니다. 데이터베이스 엔진은 SQLite를 사용합니다.
"""

QUERY_1 = """SELECT c.id, c.name, i.invoice_amt
FROM Customers AS c
LEFT JOIN Invoices AS i
ON c.id = i.customer_id
WHERE i.invoice_amt IS NULL;"""

QUERY_2 = """SELECT i.customer_id, c.name, i.invoice_amt
FROM Invoices AS i
LEFT JOIN Customers AS c
ON c.id = i.customer_id
WHERE c.name IS NULL;"""

QUERY_3 = "SQL 쿼리문을 작성해 주세요."

