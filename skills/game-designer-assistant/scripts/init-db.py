# Ініціалізація бази даних SQLite

import sqlite3
import os

def init_db():
    conn = sqlite3.connect('game_data.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sessions (
        id TEXT PRIMARY KEY,
        date TEXT,
        game_type TEXT,
        player_count INT,
        duration_min INT,
        mechanics_used TEXT,
        questions_used TEXT,
        notes TEXT,
        tags TEXT
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS mechanics (
        id TEXT PRIMARY KEY,
        name TEXT,
        description TEXT,
        status TEXT,
        first_used TEXT,
        tags TEXT
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS questions (
        id TEXT PRIMARY KEY,
        text TEXT,
        topic TEXT,
        difficulty INT,
        format TEXT,
        source TEXT,
        session_id TEXT,
        rating INT
    )
    ''')
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    print('Database initialized')
