import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='db'
)
table = 'table'

# Close the connection
conn.close()