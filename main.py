"""
ETL-Query script
"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import corn_query, oil_query

# Extract
print("Extracting data...")
extract()

# Transform and load
print("Transforming data...")
load()

# Query1
print("Querying corn-related data...")
corn_query()

# Query2
print("Querying oil-related data...")
oil_query()
