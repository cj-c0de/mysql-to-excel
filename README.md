# Convert MySQL to Excel

## Overview
MySQL to Excel is a Python utility designed to facilitate the export of MySQL database tables to Excel spreadsheets. This tool allows you to select specific tables or export an entire database with multiple sheets in a single Excel file, providing a convenient way to generate reports or backup data.

## Features
- Connect to a MySQL database using simple configuration.
- Export specific tables or all tables in a database to an Excel file.
- Supports selection of specific columns.
- Handles exceptions and errors.

## Installation
Ensure you have Python 3.x installed. Then, install the package:

```bash
pip install mysql-to-excel
```

## Usage
1. Create a Configuration:
Define your MySQL connection settings using the `MySQLConfig` model.

2. Run the Conversion:
Use the `convert_to_excel` function to export data:

```python
from mysql_to_excel import MySQLConfig, convert_to_excel

config = MySQLConfig(
    host='localhost',
    user='root',
    password='yourpassword',
    database='yourdatabase'
)

# Export a specific table
convert_to_excel(config, table='yourtable', output_file='output.xlsx', columns=['column1', 'column2'])

# Export all tables
convert_to_excel(config)
```

## License
This project is licensed under the MIT License.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs or enhancement ideas.

## Contact
- **GitHub:** [cj-c0de](https://github.com/cj-c0de)
- **Email:** dastgerdi.dev@gmail.com