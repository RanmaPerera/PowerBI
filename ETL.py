import pandas as pd

# Load raw sales data from CSV file
raw_data = pd.read_csv('raw_sales_data.csv')

# Data transformation and cleaning
# Example: Rename columns, format dates, calculate derived columns
raw_data['OrderDate'] = pd.to_datetime(raw_data['OrderDate'])
raw_data['Year'] = raw_data['OrderDate'].dt.year
raw_data['Month'] = raw_data['OrderDate'].dt.month

# Connect to the database and load the transformed data
import sqlalchemy

engine = sqlalchemy.create_engine('database_connection_string')
raw_data.to_sql('sales', engine, if_exists='replace', index=False)
