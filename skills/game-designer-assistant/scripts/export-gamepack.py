# Експорт готового набору для гри

import datetime

def export_gamepack(title, player_count, duration, mechanics, questions):
    """
    Створює markdown файл з готовим game pack.
    
    Args:
        title: назва гри
        player_count: кількість гравців
        duration: тривалість у хвилинах
        mechanics: список механік
        questions: список питань
    
    Returns:
        шлях до створеного файлу
    """
    
    filename = f"game-pack-{datetime.datetime.now().strftime('%Y%m%d')}.md"
    
    content = f"""# {title}

## Параметри
- **Кількість гравців**: {player_count}
- **Тривалість**: {duration} хв
- **Дата створення**: {datetime.datetime.now().strftime('%Y-%m-%d')}

## Механіки
"""
    
    for m in mechanics:
        content += f"- {m}\n"
    
    content += "\n## Питання\n\n"
    
    for i, q in enumerate(questions, 1):
        content += f"### {i}. {q['text']}\n"
        content += f"**Відповідь**: {q.get('answer', '')}\n\n"
    
    content += """## Правила для ведучого

[Додати короткий опис правил]

## Після гри

Не забудь записати сесію через:
```
python scripts/log-session.py
```
"""
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'Game pack exported: {filename}')
    return filename

if __name__ == '__main__':
    # Приклад
    export_gamepack(
        title='Барний квіз — 15 людей',
        player_count=15,
        duration=40,
        mechanics=['quiz-bar', 'blitz-circle'],
        questions=[
            {'text': 'Столиця України?', 'answer': 'Київ'},
            {'text': '2+2?', 'answer': '4'}
        ]
    )
