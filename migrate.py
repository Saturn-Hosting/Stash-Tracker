import sqlite3

def create_tables():
    conn = sqlite3.connect("stash_tracker.db")
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS stash (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        location TEXT NOT NULL
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS kit (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        stash_id INTEGER NOT NULL,
        FOREIGN KEY (stash_id) REFERENCES stash (id)
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS item (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        minecraft_item TEXT NOT NULL,
        kit_id INTEGER NOT NULL,
        count INTEGER NOT NULL,
        FOREIGN KEY (kit_id) REFERENCES kit (id)
    )
    """)
    
    conn.commit()
    conn.close()

create_tables()
print("Tables created successfully.")