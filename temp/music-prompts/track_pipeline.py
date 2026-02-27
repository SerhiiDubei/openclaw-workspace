#!/usr/bin/env python3
"""
Music Track Pipeline
Повний pipeline: Жанр -> Структура -> Лірика -> Style Description
"""

import random
from typing import Dict, List, Tuple, Optional
from music_genres_database import music_genres


class TrackPipeline:
    """Pipeline для генерації музичних треків"""
    
    def __init__(self):
        self.genres_db = music_genres
        
    # ========== 1. ВИБІР ЖАНРУ ==========
    
    def get_random_genre(self) -> Dict:
        """Вибирає випадковий жанр з усієї бази"""
        category = random.choice(list(self.genres_db.keys()))
        category_data = self.genres_db[category]
        
        if category_data["subcategories"]:
            subcategory = random.choice(list(category_data["subcategories"].keys()))
            genre = random.choice(category_data["subcategories"][subcategory])
            return {
                "category": category,
                "subcategory": subcategory,
                "genre": genre,
                "full_path": f"{category} > {subcategory} > {genre}"
            }
        else:
            genre = random.choice(category_data["genres"])
            return {
                "category": category,
                "subcategory": None,
                "genre": genre,
                "full_path": f"{category} > {genre}"
            }
    
    # ========== 2. ГЕНЕРАЦІЯ СТРУКТУРИ ==========
    
    def generate_structure(self, genre_info: Dict) -> Dict:
        """Генерує структуру треку на основі жанру"""
        category = genre_info["category"]
        
        # Вибираємо патерн (15+ варіацій)
        patterns = [
            # Класичні патерни
            ["Intro", "Verse", "Chorus", "Verse", "Chorus", "Outro"],
            ["Intro", "Verse", "Pre-Chorus", "Chorus", "Verse", "Pre-Chorus", "Chorus", "Outro"],
            ["Intro", "Chorus", "Verse", "Chorus", "Bridge", "Chorus", "Outro"],
            ["Verse", "Chorus", "Verse", "Chorus", "Bridge", "Chorus"],
            ["Intro", "Verse", "Chorus", "Bridge", "Chorus", "Outro"],
            
            # Розширені патерни
            ["Intro", "Verse", "Verse", "Chorus", "Verse", "Chorus", "Bridge", "Chorus", "Outro"],
            ["Intro", "Chorus", "Verse", "Chorus", "Verse", "Chorus", "Bridge", "Chorus", "Outro"],
            ["Verse", "Pre-Chorus", "Chorus", "Verse", "Pre-Chorus", "Chorus", "Bridge", "Chorus"],
            ["Intro", "Verse", "Chorus", "Verse", "Chorus", "Verse", "Chorus", "Outro"],
            ["Chorus", "Verse", "Chorus", "Bridge", "Verse", "Chorus", "Outro"],
            
            # Короткі патерни
            ["Verse", "Chorus", "Verse", "Chorus", "Outro"],
            ["Intro", "Verse", "Chorus", "Bridge", "Outro"],
            
            # Довгі/епічні патерни
            ["Intro", "Verse", "Pre-Chorus", "Chorus", "Verse", "Pre-Chorus", "Chorus", "Bridge", "Chorus", "Outro"],
            ["Intro", "Verse", "Chorus", "Verse", "Chorus", "Verse", "Chorus", "Bridge", "Chorus", "Outro"],
            
            # Альтернативні патерни
            ["Intro", "Verse", "Bridge", "Chorus", "Verse", "Bridge", "Chorus", "Outro"],
            ["Chorus", "Verse", "Bridge", "Chorus", "Verse", "Chorus", "Outro"],
            ["Intro", "Verse", "Chorus", "Instrumental", "Verse", "Chorus", "Outro"],
            
            # Специфічні для електронної музики
            ["Build", "Drop", "Break", "Build", "Drop", "Outro"],
            ["Intro", "Build", "Drop", "Breakdown", "Build", "Drop", "Outro"],
        ]
        pattern = random.choice(patterns)
        
        # Генеруємо кожну частину
        parts = []
        total_bars = 0
        
        for part_name in pattern:
            bars = self._get_bars_for_part(part_name)
            lines = bars  # 1 line per bar
            description = self._get_description(part_name, category)
            
            parts.append({
                "tag": part_name,
                "description": description,
                "bars": bars,
                "lines": lines
            })
            total_bars += bars
        
        # Розраховуємо тривалість
        duration_min = total_bars * 2 / 60  # ~2 сек на такт
        duration_max = total_bars * 4 / 60  # ~4 сек на такт
        
        return {
            "genre_info": genre_info,
            "parts": parts,
            "total_bars": total_bars,
            "estimated_duration": f"{duration_min:.1f}-{duration_max:.1f} min",
            "pattern": " -> ".join(pattern)
        }
    
    def _get_bars_for_part(self, part_name: str) -> int:
        """Повертає кількість тактів для частини"""
        bars_map = {
            "Intro": [2, 4, 8],
            "Verse": [8, 12, 16],
            "Pre-Chorus": [2, 4],
            "Chorus": [6, 8, 12],
            "Bridge": [4, 6, 8],
            "Outro": [2, 4, 8],
            # Нові частини
            "Build": [4, 8, 16],      # Build може бути довгим
            "Drop": [8, 16, 32],      # Drop — основна частина
            "Break": [2, 4, 8],       # Коротка пауза
            "Breakdown": [4, 8, 16],  # Середня за довжиною
            "Instrumental": [4, 8, 12] # Соло/інтерлюдія
        }
        return random.choice(bars_map.get(part_name, [4]))
    
    def _get_description(self, part_name: str, category: str) -> str:
        """Повертає опис для частини"""
        descriptions = {
            "Intro": {
                "Rock": ["feedback fade-in", "distorted guitar", "clean arpeggio", "drum roll"],
                "Electronic": ["synth pad swell", "build-up", "atmospheric drone"],
                "Metal": ["tremolo picking", "downtuned chugging", "dark ambience"],
                "Pop": ["catchy preview", "minimal piano", "synth stab"],
                "Hip Hop": ["vinyl crackle", "sampled melody", "808 kick roll"],
                "DEFAULT": ["atmospheric build", "rhythmic entrance", "melodic preview"]
            },
            "Verse": {
                "Rock": ["driving rhythm", "introspective vocals", "palm-muted guitars"],
                "Electronic": ["layered synths", "pulsing bass", "minimal beat"],
                "Metal": ["complex riffs", "aggressive vocals", "technical patterns"],
                "Pop": ["catchy melody", "emotional delivery", "storytelling"],
                "Hip Hop": ["lyrical flow", "storytelling", "rhythmic delivery"],
                "DEFAULT": ["narrative section", "developing theme", "building energy"]
            },
            "Pre-Chorus": {
                "Rock": ["rising tension", "instrumental build", "drum fill"],
                "Electronic": ["filter sweep", "build-up", "snare roll"],
                "Pop": ["emotional lift", "anticipation build", "rising melody"],
                "DEFAULT": ["tension building", "transition section", "energy rising"]
            },
            "Chorus": {
                "Rock": ["anthemic hook", "full band", "powerful vocals"],
                "Electronic": ["euphoric drop", "big synth lead", "dance energy"],
                "Metal": ["crushing riff", "screamed vocals", "epic hook"],
                "Pop": ["sing-along chorus", "infectious hook", "emotional peak"],
                "Hip Hop": ["catchy hook", "melodic rap", "anthemic delivery"],
                "DEFAULT": ["main hook", "climactic section", "peak energy"]
            },
            "Bridge": {
                "Rock": ["instrumental break", "tonal shift", "solo section"],
                "Electronic": ["breakdown", "rhythmic shift", "atmospheric section"],
                "Metal": ["guitar solo", "tempo change", "atmospheric break"],
                "Pop": ["emotional shift", "harmonic variation", "intimate moment"],
                "DEFAULT": ["contrast section", "departure", "tension release"]
            },
            "Outro": {
                "Rock": ["fade out", "repeated riff", "atmospheric decay"],
                "Electronic": ["filter fade", "reverb tail", "atmospheric end"],
                "Metal": ["crushing final hit", "fade to black", "sustained note"],
                "Pop": ["vocal fade", "repeated hook", "satisfying resolve"],
                "DEFAULT": ["fade out", "resolution", "final statement"]
            },
            # Нові частини для електронної музики
            "Build": {
                "Electronic": ["rising tension", "snare roll", "filter opening", "energy building"],
                "DEFAULT": ["building intensity", "rising energy", "anticipation"]
            },
            "Drop": {
                "Electronic": ["bass drop", "full energy", "peak moment", "dance explosion"],
                "DEFAULT": ["climactic moment", "peak energy", "release"]
            },
            "Break": {
                "Electronic": ["minimal beat", "stripped back", "atmospheric", "breathing space"],
                "DEFAULT": ["pause", "minimal section", "breather"]
            },
            "Breakdown": {
                "Electronic": ["stripped drums", "atmospheric pads", "build-up section", "filtered elements"],
                "DEFAULT": ["reduced arrangement", "atmospheric section"]
            },
            "Instrumental": {
                "Rock": ["guitar solo", "instrumental passage", "musical interlude"],
                "Electronic": ["synth solo", "instrumental section", "textural passage"],
                "Jazz": ["improvised solo", "instrumental exchange", "musical dialogue"],
                "DEFAULT": ["instrumental section", "musical interlude", "solo passage"]
            }
        }
        
        part_desc = descriptions.get(part_name, descriptions["Verse"])
        if category in part_desc:
            return random.choice(part_desc[category])
        return random.choice(part_desc["DEFAULT"])
    
    # ========== 3. ФОРМАТУВАННЯ ==========
    
    def format_structure_for_lyrics(self, structure: Dict) -> str:
        """Форматує структуру для генератора лірики"""
        lines = []
        for part in structure["parts"]:
            lines.append(f"[{part['tag']}] {part['description']}, {part['lines']} lines ({part['bars']} bars)")
        return " → ".join(lines)
    
    def format_meta_tags(self, structure: Dict) -> List[str]:
        """Повертає список метатегів"""
        return [f"[{part['tag']}]" for part in structure["parts"]]
    
    def generate_style_description(self, genre_info: Dict, structure: Dict) -> str:
        """Генерує style description для MusicAPI"""
        genre = genre_info["genre"]
        category = genre_info["category"]
        
        # Основний опис (перші слова - найважливіші)
        base_desc = f"{genre} style"
        
        # Додаємо характеристики категорії
        category_traits = {
            "Rock": ["electric guitars", "strong rhythm", "energetic"],
            "Electronic": ["synthesizers", "electronic beats", "atmospheric"],
            "Metal": ["heavy distortion", "powerful drums", "intense"],
            "Pop": ["catchy melodies", "polished production", "radio-friendly"],
            "Hip Hop": ["beats", "rhythmic flow", "urban"],
            "Jazz": ["improvisation", "complex harmonies", "swing"],
            "Classical": ["orchestral", "thematic", "elegant"],
            "Blues": ["guitar", "emotional", "soulful"],
            "Country": ["acoustic", "storytelling", "twang"],
            "Dance": ["four-on-the-floor", "energetic", "club-ready"],
            "Folk": ["acoustic", "traditional", "authentic"],
            "Latin": ["percussion", "rhythmic", "passionate"],
            "R&B / Soul": ["smooth", "emotional", "groove"],
            "Reggae": ["offbeat", "relaxed", "positive"],
            "World": ["ethnic", "traditional", "cultural"]
        }
        
        traits = category_traits.get(category, ["unique sound", "distinctive style"])
        traits_str = ", ".join(traits[:2])  # Беремо 2 основні
        
        # Структура треку
        structure_desc = f"{len(structure['parts'])} sections"
        
        # Збираємо все (макс 400 символів для MusicAPI)
        description = f"{base_desc} with {traits_str}, {structure_desc}, professional production"
        
        return description[:400]  # Обмеження MusicAPI
    
    # ========== 4. ПОВНИЙ PIPELINE ==========
    
    def generate_full_track(self, category: str = None) -> Dict:
        """Генерує повний трек: жанр + структура + опис"""
        # 1. Вибираємо жанр
        if category:
            genre_info = self.get_genre_by_category(category)
        else:
            genre_info = self.get_random_genre()
        
        # 2. Генеруємо структуру
        structure = self.generate_structure(genre_info)
        
        # 3. Генеруємо описи
        style_description = self.generate_style_description(genre_info, structure)
        
        return {
            "genre_info": genre_info,
            "structure": structure,
            "style_description": style_description,
            "lyrics_structure": self.format_structure_for_lyrics(structure),
            "meta_tags": self.format_meta_tags(structure)
        }
    
    def get_genre_by_category(self, category: str) -> Dict:
        """Вибирає випадковий жанр з конкретної категорії"""
        if category not in self.genres_db:
            raise ValueError(f"Категорія '{category}' не знайдена")
        
        category_data = self.genres_db[category]
        
        if category_data["subcategories"]:
            subcategory = random.choice(list(category_data["subcategories"].keys()))
            genre = random.choice(category_data["subcategories"][subcategory])
            return {
                "category": category,
                "subcategory": subcategory,
                "genre": genre,
                "full_path": f"{category} > {subcategory} > {genre}"
            }
        else:
            genre = random.choice(category_data["genres"])
            return {
                "category": category,
                "subcategory": None,
                "genre": genre,
                "full_path": f"{category} > {genre}"
            }


# Приклад використання
if __name__ == "__main__":
    pipeline = TrackPipeline()
    
    print("=" * 60)
    print("ПРИКЛАД 1: Випадковий трек")
    print("=" * 60)
    
    track = pipeline.generate_full_track()
    
    print(f"\nЖанр: {track['genre_info']['full_path']}")
    print(f"Style Description: {track['style_description']}")
    print(f"\nСтруктура треку:")
    print(track['lyrics_structure'])
    print(f"\nМетатеги: {' '.join(track['meta_tags'])}")
    print(f"Тривалість: {track['structure']['estimated_duration']}")
    
    print("\n" + "=" * 60)
    print("ПРИКЛАД 2: Трек категорії 'Electronic'")
    print("=" * 60)
    
    track2 = pipeline.generate_full_track("Electronic")
    
    print(f"\nЖанр: {track2['genre_info']['full_path']}")
    print(f"Style Description: {track2['style_description']}")
    print(f"\nСтруктура треку:")
    print(track2['lyrics_structure'])
