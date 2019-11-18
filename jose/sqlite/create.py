import sqlite3
from sqlite3 import Error
 
 
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
 
    return conn

def create_tables(conn):
    sql_query = """CREATE TABLE nenes (
                id INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                edad INTEGER NOT NULL,
                esta_registrado INTEGER NOT NULL,
                karma INTEGER NOT NULL
            );"""

    cur = conn.cursor()
    cur.execute(sql_query)
 
 
if __name__ == '__main__':
    conn = create_connection("./persistence/pythonsqlite.db")
    create_tables(conn)
