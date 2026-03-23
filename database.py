import sqlite3

class Database:
    def __init__(self, db_name="finance.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL,
                category TEXT,
                type TEXT,
                description TEXT,
                date TEXT
            )
        ''')
        self.conn.commit()

    def insert(self, transaction):
        self.conn.execute('''
            INSERT INTO transactions (amount, category, type, description, date)
            VALUES (?, ?, ?, ?, ?)
        ''', (transaction.amount, transaction.category,
              transaction.t_type, transaction.description, transaction.date))
        self.conn.commit()

    def fetch_all(self):
        cursor = self.conn.execute("SELECT * FROM transactions")
        return cursor.fetchall()
    
    def close(self):
        self.conn.close()