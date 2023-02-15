import sqlite3 as sl

connect = sl.connect('ulta.db')
cur = connect.cursor()

with connect:
    cur.execute("""
        CREATE TABLE IF NOT EXISTS ulta (
            id INTEGER  PRIMARY KEY,
            password INTEGER,
            username Text 
        );
        """)
connect.commit()
cur.close()