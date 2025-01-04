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
query = f'SELECT * FROM {table}'
data = pd.read_sql(query, conn)

# Save data to Excel
with pd.ExcelWriter(f'{table}.xlsx') as writer:
    data.to_excel(writer, index=False)

# Close the connection
conn.close()