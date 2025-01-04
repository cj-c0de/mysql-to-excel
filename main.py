from dataclasses import dataclass
import mysql.connector
import pandas as pd

@dataclass
class MySQLConfig:
    host: str
    user: str
    password: str
    database: str

def convert_to_excel(config: MySQLConfig, table: str, output_file: str, columns: list = None):
    # Connect to MySQL database
    conn = mysql.connector.connect(
        host=config.host,
        user=config.user,
        password=config.password,
        database=config.database
    )

    # Fetch data from table
    if columns:
        columns_str = ', '.join(columns)
    else:
        columns_str = '*'
    query = f'SELECT {columns_str} FROM {table}'
    data = pd.read_sql(query, conn)

    # Save data to Excel
    with pd.ExcelWriter(output_file) as writer:
        data.to_excel(writer, index=False)

    # Close the connection
    conn.close()