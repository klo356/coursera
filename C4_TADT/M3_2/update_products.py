#!/usr/bin/env python3
import argparse
import csv
import sqlite3
import sys

def process_options():
    arg_parser = argparse.ArgumentParser(
        description='Update products CSV into the specified database'
    )
    arg_parser.add_argument('--server', default='products')
    arg_parser.add_argument('filename', default='new_products.csv')
    args = arg_parser.parse_args()
    return args

def database_connection(name):
    db = sqlite3.connect(f'{name}.db', isolation_level='DEFERRED')
    cursor = db.cursor()
    # Check if the table is already present
    cursor.execute("""
    SELECT name FROM sqlite_master WHERE type='table' AND
    name='products'
    """)
    if cursor.fetchone() is None:
        cursor.execute("""
            CREATE TABLE products
            (product_code, description)
            """)
    return db

def update_data(database, options):
    with open(options.filename, 'r') as products:
        reader = csv.DictReader(products)
        cursor = database.cursor()
        for row in reader:
            print('Updating {} with value: {}'.format(
                row['product_code'], row['description']))
            cursor.execute("""
            INSERT OR REPLACE INTO products
            (product_code, description)
            VALUES (?, ?)
            """, (row['product_code'], row['description']))
        database.commit()
        database.close()
        print('Database updated successfully')
        return 0

if __name__ == '__main__':
    options = process_options()
    database = database_connection(options.server)
    sys.exit(update_data(database, options))
