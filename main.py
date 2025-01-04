import mysql.connector
import pandas as pd

def convert_to_excel(host, user, password, database, table, output_file):
    # Connect to MySQL database
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    # Fetch data from table
    query = f'SELECT * FROM {table}'
    data = pd.read_sql(query, conn)

    # Save data to Excel
    with pd.ExcelWriter(output_file) as writer:
        data.to_excel(writer, index=False)

    # Close the connection
    conn.close()