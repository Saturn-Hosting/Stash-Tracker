import sqlite3

conn = sqlite3.connect('stash_tracker.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS stash (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    location TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS kit (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    stash_id INTEGER NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (stash_id) REFERENCES stash (id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS item (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    kit_id INTEGER NOT NULL,
    count INTEGER NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (kit_id) REFERENCES kit (id)
)
''')

conn.commit()
conn.close()