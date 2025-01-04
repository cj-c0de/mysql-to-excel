import mysql.connector
import pandas as pd

# Connect to MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='db'
)
table = 'table'

# Fetch data from table
query = f"SELECT * FROM {table}"
data = pd.read_sql(query, conn)

# Close the connection
conn.close()