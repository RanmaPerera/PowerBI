import pandas as pd
import sqlalchemy

# Replace these placeholders with your MySQL server details
username = 'root'
password = ' '
host = 'localhost'  # If your MySQL server is running locally
port = '3306'  # Default MySQL port
database_name = 'powerbi'

# Construct the MySQL connection string
connection_string = f"mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database_name}"

# Create a database engine using the connection string
engine = sqlalchemy.create_engine(connection_string)

# Load raw sales data from CSV file
raw_data = pd.read_csv('raw_sales_data.csv')

# Data transformation and cleaning
# Example: Rename columns, format dates, calculate derived columns
raw_data['OrderDate'] = pd.to_datetime(raw_data['OrderDate'])
raw_data['Year'] = raw_data['OrderDate'].dt.year
raw_data['Month'] = raw_data['OrderDate'].dt.month

# Replace 'your_table_name' with the name of your target table in the MySQL database
table_name = 'sales'

# Load the transformed data into the MySQL database
raw_data.to_sql(table_name, engine, if_exists='replace', index=False)

# Close the database connection
engine.dispose()

print(f"Data has been loaded into the '{table_name}' table.")