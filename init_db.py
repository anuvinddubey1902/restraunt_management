import sqlite3

DATABASE = 'menu.db'

conn = sqlite3.connect(DATABASE)
cur = conn.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS menu (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    food_name TEXT NOT NULL,
    price REAL NOT NULL,
    in_stock TEXT NOT NULL
)
''')
conn.commit()
conn.close()

print("Database initialized.")
