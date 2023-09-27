"""Query the database"""

import sqlite3


def corn_query():
    """Query the database for the top 5 rows of the GroceryDB table"""
    conn = sqlite3.connect("GroceryDB.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT general_name, count_products FROM GroceryDB WHERE semantic_tree_name == 'corn'"
    )
    print(
        "Top 5 rows of names and counts from GroceryDB table in the corn semantic tree:"
    )
    print(cursor.fetchall())
    conn.close()
    return "Success"


def oil_query():
    """Query the database for the top 5 rows of the GroceryDB table"""
    conn = sqlite3.connect("GroceryDB.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT general_name, count_products FROM GroceryDB WHERE semantic_tree_name == 'oil'"
    )
    print(
        "Top 5 rows of names and counts from GroceryDB table in the oil semantic tree:"
    )
    print(cursor.fetchall())
    conn.close()
    return "Success"
