import sqlite3
import os

def init_db():
    """Ініціалізація бази — тільки 3 таблиці для бета"""
    
    db_path = os.path.join(os.path.dirname(__file__), '..', 'game_data.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Таблиця механік
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS mechanics (
        id TEXT PRIMARY KEY,
        name TEXT,
        description TEXT,
        status TEXT DEFAULT 'draft'  -- draft | tested | approved
    )
    ''')
    
    # Таблиця питань
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS questions (
        id TEXT PRIMARY KEY,
        text TEXT,
        topic TEXT,
        difficulty INTEGER CHECK(difficulty BETWEEN 1 AND 5),
        format TEXT,  -- bar | blitz | circle | yesno | donetki
        times_used INTEGER DEFAULT 0,
        rating INTEGER CHECK(rating BETWEEN 1 AND 5)
    )
    ''')
    
    # Таблиця сесій
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sessions (
        id TEXT PRIMARY KEY,
        date TEXT,
        game_type TEXT,  -- bar | home | corporate
        player_count INTEGER,
        duration_min INTEGER,
        mechanics_used TEXT,  -- JSON array
        what_worked TEXT,
        what_didnt TEXT
    )
    ''')
    
    conn.commit()
    conn.close()
    print('Database initialized (3 tables)')

if __name__ == '__main__':
    init_db()
