#!/usr/bin/env python3
"""
Storage Cleanup Script
Переміщує файли з кирилиці в латиницю, видаляє дублікати
"""

import os
import sys

# Додаємо шлях до модулів
sys.path.insert(0, '/root/.openclaw/workspace/temp/music-prompts')

from music_genres_database import music_genres

def transliterate_cyrillic(text):
    """Транслітерація кирилиці в латиницю (українська/російська)"""
    mapping = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'h', 'д': 'd', 'е': 'e', 'ё': 'yo',
        'ж': 'zh', 'з': 'z', 'и': 'y', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm',
        'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
        'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
        'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya',
        'і': 'i', 'ї': 'yi', 'є': 'ye', 'ґ': 'g'
    }
    
    result = ''
    for char in text.lower():
        if char in mapping:
            result += mapping[char]
        else:
            result += char
    return result

def normalize_username(username):
    """Нормалізує ім'я користувача"""
    # Транслітерація
    username = transliterate_cyrillic(username)
    # Пробіли → підкреслення
    username = username.replace(' ', '_')
    # Видаляємо спецсимволи
    username = ''.join(c for c in username if c.isalnum() or c in '_-')
    return username

if __name__ == "__main__":
    # Тест
    test_names = [
        "Роман Романюк",
        "Serhii Dubei",
        "Dmytro Churilov",
        "Анна Иванова"
    ]
    
    for name in test_names:
        print(f"{name} → {normalize_username(name)}")
