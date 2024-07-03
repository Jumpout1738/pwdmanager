import sqlite3
import os

def create_connection():
    """Create and return a connection to the SQLite database."""
    db_path = 'data/passwords.db'
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_path)
        print(f"Successfully connected to the database at {db_path}")
        return conn
    except sqlite3.Error as e:
        print(e)
        return None

def create_table(conn):
    """Create the passwords table if it doesn't exist."""
    sql_create_table = """
    CREATE TABLE IF NOT EXISTS passwords (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        site_name TEXT NOT NULL,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    );"""
    conn.execute(sql_create_table)
    conn.commit()

def add_password(conn, site_name, username, encrypted_password):
    """Add a new password record to the database."""
    sql_insert = """
    INSERT INTO passwords (site_name, username, password)
    VALUES (?, ?, ?);"""
    conn.execute(sql_insert, (site_name, username, encrypted_password))
    conn.commit()

def get_all_passwords(conn):
    """Retrieve all password records from the database."""
    sql_select = "SELECT * FROM passwords"
    cursor = conn.execute(sql_select)
    return cursor.fetchall()
