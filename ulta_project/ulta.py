import sqlite3 as sl

connect = sl.connect('ulta.db')
cur = connect.cursor()

with connect:
    cur.execute("""
        CREATE TABLE IF NOT EXISTS ulta (
            id INTEGER,
            image IMAGE
            url TEXT,
            name TEXT,
            price INTEGER,
            sale INTEGER
        );
        """)
connect.commit()
cur.close()