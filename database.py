import sqlite3
con = sqlite3.connect('database.db', check_same_thread=False)
c = con.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS tasks("""
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          title TEXT NOT NULL,
          description TEXT,
          status TEXT NOT NULL DEFAULT 'pending'
          """)''')
con.commit()