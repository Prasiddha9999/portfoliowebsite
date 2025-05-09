import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Connect to PostgreSQL server
conn = psycopg2.connect(
    dbname='postgres',
    user='postgres',
    password='1234',  # Use the password from your settings.py
    host='localhost',
    port='5432'
)

conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = conn.cursor()

# Check if database exists
cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'portfolio'")
exists = cursor.fetchone()

if not exists:
    # Create database
    cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier('portfolio')))
    print("Database 'portfolio' created successfully")
else:
    print("Database 'portfolio' already exists")

# Close connection
cursor.close()
conn.close()

print("Database setup completed")
