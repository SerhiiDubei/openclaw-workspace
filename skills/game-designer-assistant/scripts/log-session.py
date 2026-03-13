# Логування сесії після гри

import sqlite3
import json
import datetime

def log_session(game_type, player_count, duration, mechanics, worked, didnt):
    """
    Записує сесію в базу після гри.
    
    Args:
        game_type: 'bar' | 'home' | 'corporate'
        player_count: int
        duration: int (хвилин)
        mechanics: list of strings
        worked: що спрацювало
        didnt: що не спрацювало
    """
    conn = sqlite3.connect('game_data.db')
    cursor = conn.cursor()
    
    session_id = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
    date = datetime.datetime.now().isoformat()
    
    cursor.execute('''
    INSERT INTO sessions (id, date, game_type, player_count, duration_min, mechanics_used, what_worked, what_didnt)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (session_id, date, game_type, player_count, duration, json.dumps(mechanics), worked, didnt))
    
    conn.commit()
    conn.close()
    print(f'Session logged: {session_id}')

if __name__ == '__main__':
    # Приклад використання
    log_session(
        game_type='bar',
        player_count=15,
        duration=40,
        mechanics=['quiz-bar', 'blitz-circle'],
        worked='Швидка зміна ходів, соціальна взаємодія',
        didnt='Занадто довгі пояснення правил'
    )
