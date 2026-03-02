import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="shrawani",
    password="Shrawani@1606",
    database="superstore_project"
)

cursor = conn.cursor()

query = """
SELECT category, SUM(sales)
FROM superstore
GROUP BY category;
"""

cursor.execute(query)

for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()