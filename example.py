from mysql_to_excel import convert_to_excel,MySQLConfig

convert_to_excel(
    config=MySQLConfig(
        host='localhost',
        user='root',
        password='',
        database='db_name'
    ),
    table='table_name',
    output_file='file_name.xlsx',
    columns=['id','title']
)