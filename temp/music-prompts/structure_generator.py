#!/usr/bin/env python3
"""
Music Structure Generator
Генератор структур пісень на основі жанру та стилю
"""

import random
from typing import List, Dict, Tuple

# Категорії та жанри з Airtable
MUSIC_CATEGORIES = {
    "ROCK": ["Alternative Rock", "Indie Rock", "Progressive Rock", "Southern Rock", "Surf Rock"],
    "ELECTRONIC": ["Techno", "House", "Trance", "Dubstep", "Ambient", "Synthwave"],
    "METAL": ["Thrash Metal", "Doom Metal", "Progressive Metal", "Death Metal"],
    "POP": ["Teen Pop", "Dance Pop", "Electropop", "Indie Pop"],
    "JAZZ": ["Bebop", "Smooth Jazz", "Fusion", "Swing"],
    "HIP_HOP": ["Alternative Hip Hop", "Trap", "Boom Bap", "Lo-Fi"],
    "WORLD": ["Celtic", "Arabic", "Latin", "African", "Indian"],
    "CLASSICAL": ["Baroque", "Romantic", "Modern Classical", "Serialism"],
    "ALTERNATIVE": ["Post-Rock", "Math Rock", "Noise Rock"],
    "FOLK": ["Traditional Folk", "Indie Folk", "Folk Rock"],
    "RNB": ["Contemporary R&B", "Neo Soul", "Alternative R&B"],
    "COUNTRY": ["Traditional Country", "Alt-Country", "Bluegrass"],
    "BLUES": ["Texas Blues", "Chicago Blues", "Delta Blues"],
    "REGGAE": ["Roots Reggae", "Dub", "Dancehall"],
    "PUNK": ["Pop Punk", "Hardcore", "Post-Punk"],
    "LATIN": ["Salsa", "Bachata", "Reggaeton", "Cumbia"],
    "FUNK": ["P-Funk", "Funk Rock", "Electro Funk"]
}

# Метатеги для частин пісні
SONG_PARTS = {
    "Intro": {
        "duration_bars": [2, 4, 8],
        "lines_per_bar": 1,
        "descriptions": {
            "ROCK": ["feedback fade-in", "distorted guitar riff", "clean arpeggio", "ambient texture"],
            "ELECTRONIC": ["synth pad swell", "rhythmic build-up", "atmospheric drone", "filtered beat"],
            "METAL": ["tremolo picking", "downtuned chugging", "symphonic intro", "dark ambience"],
            "POP": ["catchy hook preview", "minimal piano", "synth stab", "vocal sample"],
            "JAZZ": ["brass section intro", "walking bass line", "piano comping", "brush drums"],
            "HIP_HOP": ["vinyl crackle", "sampled melody", "808 kick roll", "ad-libs"],
            "DEFAULT": ["atmospheric build", "rhythmic entrance", "melodic preview", "textural start"]
        }
    },
    "Verse": {
        "duration_bars": [8, 12, 16],
        "lines_per_bar": 1,
        "descriptions": {
            "ROCK": ["driving rhythm section", "introspective vocals", "palm-muted guitars", "dynamic storytelling"],
            "ELECTRONIC": ["layered synths", "pulsing bass", "minimal beat", "atmospheric pads"],
            "METAL": ["complex riffs", "aggressive vocals", "blast beats", "technical patterns"],
            "POP": ["catchy melody", "emotional delivery", "rhythmic vocals", "storytelling"],
            "JAZZ": ["improvised solo", "call and response", "swing rhythm", "complex harmonies"],
            "HIP_HOP": ["lyrical flow", "storytelling", "rhythmic delivery", "wordplay"],
            "DEFAULT": ["narrative section", "developing theme", "building energy", "lyrical content"]
        }
    },
    "Pre-Chorus": {
        "duration_bars": [2, 4],
        "lines_per_bar": 1,
        "descriptions": {
            "ROCK": ["rising tension", "instrumental build", "dynamic shift", "energy increase"],
            "ELECTRONIC": ["filter sweep", "build-up", "rising synth", "tension"],
            "METAL": ["tempo acceleration", "intensity build", "breakdown prep", "atmospheric tension"],
            "POP": ["emotional lift", "harmonic shift", "anticipation build", "rising melody"],
            "DEFAULT": ["tension building", "transition section", "energy rising", "anticipation"]
        }
    },
    "Chorus": {
        "duration_bars": [6, 8, 12],
        "lines_per_bar": 1,
        "descriptions": {
            "ROCK": ["anthemic hook", "full band explosion", "powerful vocals", "catchy melody"],
            "ELECTRONIC": ["euphoric drop", "big synth lead", "dance energy", "peak moment"],
            "METAL": ["crushing riff", "screamed vocals", "double bass", "epic hook"],
            "POP": ["sing-along chorus", "infectious hook", "emotional peak", "catchy melody"],
            "JAZZ": ["ensemble section", "harmonic richness", "swing peak", "collective improv"],
            "HIP_HOP": ["catchy hook", "melodic rap", "anthemic delivery", "memorable phrase"],
            "DEFAULT": ["main hook", "climactic section", "memorable moment", "peak energy"]
        }
    },
    "Bridge": {
        "duration_bars": [4, 6, 8],
        "lines_per_bar": 1,
        "descriptions": {
            "ROCK": ["instrumental break", "tonal shift", "solo section", "dynamic contrast"],
            "ELECTRONIC": ["breakdown", "rhythmic shift", "atmospheric section", "build-up"],
            "METAL": ["guitar solo", "tempo change", "atmospheric break", "technical display"],
            "POP": ["emotional shift", "harmonic variation", "intimate moment", "contrast section"],
            "DEFAULT": ["contrast section", "departure", "tension release", "variation"]
        }
    },
    "Outro": {
        "duration_bars": [2, 4, 8],
        "lines_per_bar": 1,
        "descriptions": {
            "ROCK": ["fade out", "repeated riff", "atmospheric decay", "feedback end"],
            "ELECTRONIC": ["filter fade", "reverb tail", "beat drop out", "atmospheric end"],
            "METAL": ["crushing final hit", "fade to black", "ambient outro", "sustained note"],
            "POP": ["vocal fade", "repeated hook", "minimal ending", "satisfying resolve"],
            "DEFAULT": ["fade out", "resolution", "textural decay", "final statement"]
        }
    }
}

# Структурні патерни (варіації)
STRUCTURE_PATTERNS = [
    ["Intro", "Verse", "Chorus", "Verse", "Chorus", "Bridge", "Chorus", "Outro"],
    ["Intro", "Verse", "Pre-Chorus", "Chorus", "Verse", "Pre-Chorus", "Chorus", "Outro"],
    ["Intro", "Chorus", "Verse", "Chorus", "Bridge", "Chorus", "Outro"],
    ["Verse", "Chorus", "Verse", "Chorus", "Bridge", "Chorus"],
    ["Intro", "Verse", "Chorus", "Bridge", "Chorus", "Outro"],
]


def get_description(part: str, category: str) -> str:
    """Отримати опис для частини пісні на основі категорії"""
    descriptions = SONG_PARTS[part]["descriptions"]
    if category in descriptions:
        return random.choice(descriptions[category])
    return random.choice(descriptions["DEFAULT"])


def generate_structure(genre: str, category: str = None) -> Dict:
    """
    Генерує структуру пісні для заданого жанру
    
    Args:
        genre: Назва жанру (наприклад, "Alternative Rock")
        category: Категорія (наприклад, "ROCK") — якщо None, визначається автоматично
    
    Returns:
        Dict з повною структурою пісні
    """
    # Визначаємо категорію якщо не вказана
    if category is None:
        for cat, genres in MUSIC_CATEGORIES.items():
            if genre in genres:
                category = cat
                break
        if category is None:
            category = "DEFAULT"
    
    # Вибираємо рандомний патерн структури
    pattern = random.choice(STRUCTURE_PATTERNS)
    
    # Генеруємо деталі для кожної частини
    structure_parts = []
    total_bars = 0
    
    for part_name in pattern:
        part_config = SONG_PARTS[part_name]
        
        # Випадкова кількість тактів
        bars = random.choice(part_config["duration_bars"])
        lines = bars * part_config["lines_per_bar"]
        
        # Опис для цієї категорії
        description = get_description(part_name, category)
        
        structure_parts.append({
            "tag": part_name,
            "description": description,
            "bars": bars,
            "lines": lines
        })
        
        total_bars += bars
    
    # Розраховуємо приблизну тривалість (1 такт ≈ 2-4 секунди в залежності від темпу)
    estimated_duration_sec = total_bars * 3  # середнє значення
    estimated_duration_min = estimated_duration_sec / 60
    
    return {
        "genre": genre,
        "category": category,
        "structure": structure_parts,
        "total_bars": total_bars,
        "estimated_duration": f"{estimated_duration_min:.1f}-{estimated_duration_min + 1:.1f} min",
        "pattern_used": " → ".join(pattern)
    }


def format_structure_for_lyrics(structure: Dict) -> str:
    """Форматує структуру для генератора лірики"""
    lines = []
    for part in structure["structure"]:
        lines.append(f"[{part['tag']}] {part['description']}, {part['lines']} lines ({part['bars']} bars)")
    return " → ".join(lines)


def format_meta_tags(structure: Dict) -> List[str]:
    """Повертає список метатегів для кожної частини"""
    return [f"[{part['tag']}]" for part in structure["structure"]]


# Приклад використання
if __name__ == "__main__":
    # Тест генерації
    test_genres = ["Alternative Rock", "Techno", "Thrash Metal", "Trap"]
    
    for genre in test_genres:
        print(f"\n{'='*60}")
        print(f"Жанр: {genre}")
        print('='*60)
        
        result = generate_structure(genre)
        
        print(f"Категорія: {result['category']}")
        print(f"Тривалість: {result['estimated_duration']}")
        print(f"Всього тактів: {result['total_bars']}")
        print(f"\nСтруктура:")
        print(format_structure_for_lyrics(result))
        print(f"\nМетатеги: {' '.join(format_meta_tags(result))}")
