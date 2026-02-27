# Music Genres Database
# Повна таблиця жанрів з musicgenreslist.com
# Структура: Категорія -> Підкатегорія (якщо є) -> Жанр

music_genres = {
    "Alternative": {
        "subcategories": None,
        "genres": [
            "Art Punk", "Alternative Rock", "Britpunk", "College Rock", "Crossover Thrash",
            "Crust Punk", "Emotional Hardcore (emo / emocore)", "Experimental Rock",
            "Folk Punk", "Goth / Gothic Rock", "Grunge", "Hardcore Punk", "Hard Rock",
            "Indie Rock", "Lo-fi", "Musique Concrète", "New Wave", "Progressive Rock",
            "Punk", "Shoegaze", "Steampunk"
        ]
    },
    
    "Anime": {
        "subcategories": None,
        "genres": ["Anime"]
    },
    
    "Blues": {
        "subcategories": None,
        "genres": [
            "Acoustic Blues", "African Blues", "Blues Rock", "Blues Shouter", "British Blues",
            "Canadian Blues", "Chicago Blues", "Classic Blues", "Classic Female Blues",
            "Contemporary Blues", "Contemporary R&B", "Country Blues", "Dark Blues",
            "Delta Blues", "Detroit Blues", "Doom Blues", "Electric Blues", "Folk Blues",
            "Gospel Blues", "Harmonica Blues", "Hill Country Blues", "Hokum Blues",
            "Jazz Blues", "Jump Blues", "Kansas City Blues", "Louisiana Blues",
            "Memphis Blues", "Modern Blues", "New Orlean Blues", "NY Blues", "Piano Blues",
            "Piedmont Blues", "Punk Blues", "Ragtime Blues", "Rhythm Blues", "Soul Blues",
            "St. Louis Blues", "Swamp Blues", "Texas Blues", "Urban Blues", "Vandeville",
            "West Coast Blues", "Zydeco"
        ]
    },
    
    "Children's Music": {
        "subcategories": None,
        "genres": ["Lullabies", "Sing-Along", "Stories"]
    },
    
    "Classical": {
        "subcategories": {
            "Chamber Music": ["String Quartet"]
        },
        "genres": [
            "Avant-Garde", "Ballet", "Baroque", "Cantata", "Chant", "Choral",
            "Classical Crossover", "Concerto", "Concerto Grosso", "Contemporary Classical",
            "Early Music", "Expressionist", "High Classical", "Impressionist",
            "Mass Requiem", "Medieval", "Minimalism", "Modern Composition",
            "Modern Classical", "Opera", "Oratorio", "Orchestral", "Organum",
            "Renaissance", "Romantic (early period)", "Romantic (later period)",
            "Sonata", "Symphonic", "Symphony", "Twelve-tone", "Wedding Music"
        ]
    },
    
    "Comedy": {
        "subcategories": None,
        "genres": [
            "Novelty", "Parody Music", "Stand-up Comedy", "Vaudeville"
        ]
    },
    
    "Commercial": {
        "subcategories": None,
        "genres": ["Jingles", "TV Themes"]
    },
    
    "Country": {
        "subcategories": {
            "Bluegrass": ["Progressive Bluegrass", "Reactionary Bluegrass", "Traditional Bluegrass"]
        },
        "genres": [
            "Alternative Country", "Americana", "Australian Country", "Bakersfield Sound",
            "Blues Country", "Cajun Fiddle Tunes", "Christian Country", "Classic Country",
            "Close Harmony", "Contemporary Bluegrass", "Contemporary Country",
            "Country Gospel", "Country Pop", "Country Rap", "Country Rock", "Country Soul",
            "Cowboy / Western", "Cowpunk", "Dansband", "Honky Tonk", "Franco-Country",
            "Gulf and Western", "Hellbilly Music", "Instrumental Country", "Lubbock Sound",
            "Nashville Sound", "Neotraditional Country", "Outlaw Country", "Progressive",
            "Psychobilly / Punkabilly", "Red Dirt", "Sertanejo", "Texas County",
            "Traditional Country", "Truck-Driving Country", "Urban Cowboy",
            "Western Swing", "Zydeco"
        ]
    },
    
    "Dance": {
        "subcategories": {
            "Breakbeat / Breakstep": [
                "4-Beat", "Acid Breaks", "Baltimore Club", "Big Beat", "Breakbeat Hardcore",
                "Broken Beat", "Florida Breaks", "Nu Skool Breaks"
            ],
            "Hardcore": [
                "Bouncy House", "Bouncy Techno", "Breakcore", "Digital Hardcore", "Doomcore",
                "Dubstyle", "Gabber", "Happy Hardcore", "Hardstyle", "Jumpstyle",
                "Makina", "Speedcore", "Terrorcore", "Uk Hardcore"
            ],
            "House": [
                "Acid House", "Chicago House", "Deep House", "Diva House", "Dutch House",
                "Electro House", "Freestyle House", "French House", "Funky House",
                "Ghetto House", "Hardbag", "Hip House", "Italo House", "Latin House",
                "Minimal House", "Progressive House", "Rave Music", "Swing House",
                "Tech House", "Tribal House", "Tropical House", "UK Hard House",
                "US Garage", "Vocal House"
            ],
            "Techno": [
                "Acid Techno", "Detroit Techno", "Free Tekno", "Ghettotech", "Minimal",
                "Nortec", "Schranz", "Techno-Dnb", "Technopop", "Tecno Brega", "Toytown Techno"
            ],
            "Trance": [
                "Acid Trance", "Acid-House", "Classic Trance", "Dark Psy", "Deep House",
                "Dream Trance", "Hard Trance", "Minimal Techno", "Prog. Trance",
                "Psy-Trance", "Tech House", "Tech Trance", "Vocal Trance"
            ]
        },
        "genres": [
            "Club / Club Dance", "Breakcore", "Brostep", "Chillstep", "Deep House",
            "Dubstep", "Electro House", "Electroswing", "Exercise", "Future Garage",
            "Garage", "Glitch Hop", "Glitch Pop", "Grime", "Hard Dance", "Hi-NRG / Eurodance",
            "Horrorcore", "Jackin House", "Jungle / Drum'n'bass", "Liquid Dub", "Regstep",
            "Speedcore", "Trap"
        ]
    },
    
    "Disney": {
        "subcategories": None,
        "genres": ["Disney"]
    },
    
    "Easy Listening": {
        "subcategories": None,
        "genres": [
            "Background", "Bop", "Elevator", "Furniture", "Lounge",
            "Middle of the Road", "Swing"
        ]
    },
    
    "Electronic": {
        "subcategories": {
            "Ambient": [
                "Ambient Dub", "Ambient House", "Ambient Techno", "Dark Ambient",
                "Drone Music", "Illbient", "Isolationism", "Lowercase"
            ],
            "Chiptune": [
                "Bitpop", "Game Boy", "Nintendocore", "Video Game Music", "Yorkshire Bleeps and Bass"
            ],
            "Downtempo": [
                "Acid Jazz", "Balearic Beat", "Chill Out", "Dub Music", "Dubtronica",
                "Ethnic Electronica", "Moombahton", "Nu Jazz", "Trip Hop"
            ],
            "Drum & Bass": [
                "Darkcore", "Darkstep", "Drumfunk", "Drumstep", "Hardstep",
                "Intelligent Drum and Bass", "Jump-Up", "Liquid Funk", "Neurofunk",
                "Oldschool Jungle", "Darkside Jungle", "Ragga Jungle", "Raggacore",
                "Sambass", "Techstep"
            ],
            "Electro": [
                "Crunk", "Electro Backbeat", "Electro-Grime", "Electropop"
            ],
            "Electroacoustic": [
                "Acousmatic Music", "Computer Music", "Electroacoustic Improvisation",
                "Field Recording", "Live Coding", "Live Electronics",
                "Soundscape Composition", "Tape Music"
            ],
            "Electronica": [
                "Berlin School", "Chillwave", "Electronic Art Music", "Electronic Dance Music",
                "Folktronica", "Freestyle Music", "Glitch", "Idm", "Laptronica",
                "Skweee", "Sound Art", "Synthcore"
            ],
            "Electronic Rock": [
                "Alternative Dance", "Baggy", "Madchester", "Dance-Punk", "Dance-Rock",
                "Dark Wave", "Electroclash", "Electropunk", "Ethereal Wave", "Indietronica"
            ]
        },
        "genres": [
            "2-Step", "8bit", "Asian Underground", "Bassline", "Chillwave", "Crunk",
            "Electro-swing", "Eurodance", "Hard Bounce", "Hard NRG", "Industrial",
            "New Rave", "Synthpop", "Synthwave", "Witch House"
        ]
    },
    
    "Enka": {
        "subcategories": None,
        "genres": ["Enka"]
    },
    
    "French Pop": {
        "subcategories": None,
        "genres": ["French Pop", "French Rock", "French Hip Hop", "French Electro"]
    },
    
    "Folk": {
        "subcategories": {
            "American Folk": ["Appalachian", "Cajun", "Zydeco"],
            "Celtic": ["Celtic Folk", "Irish Folk", "Scottish Folk", "Welsh Folk"],
            "European Folk": ["Balkan", "Klezmer", "Polka", "Romani"],
            "World Folk": ["African Folk", "Asian Folk", "Latin Folk", "Middle Eastern Folk"]
        },
        "genres": [
            "Anti-Folk", "Contemporary Folk", "Folk Revival", "Folk Rock",
            "Folk-Pop", "Folktronica", "Indie Folk", "Industrial Folk",
            "Neofolk", "Progressive Folk", "Psychedelic Folk", "Singer-Songwriter",
            "Traditional Folk", "Urban Folk"
        ]
    },
    
    "German Folk": {
        "subcategories": None,
        "genres": ["German Folk", "Oompah", "Schlager", "Volksmusik"]
    },
    
    "German Pop": {
        "subcategories": None,
        "genres": ["German Pop", "German Rock", "Deutschrap", "Neue Deutsche Welle"]
    },
    
    "Hip Hop": {
        "subcategories": {
            "Alternative Hip Hop": ["Abstract Hip Hop", "Alternative Rap", "Conscious Hip Hop", "Jazz Rap"],
            "East Coast": ["Boom Bap", "Hardcore Hip Hop", "Mafioso Rap", "New School"],
            "Experimental": ["Cloud Rap", "Emo Rap", "Glitch Hop", "Industrial Hip Hop"],
            "Old School": ["Old School Hip Hop", "Party Rap"],
            "Southern": ["Atlanta Hip Hop", "Bounce", "Crunk", "Dirty South", "Memphis Rap", "Miami Bass", "Trap"],
            "West Coast": ["G-Funk", "Hyphy", "West Coast Hip Hop"]
        },
        "genres": [
            "Battle Rap", "British Hip Hop", "Christian Hip Hop", "Comedy Hip Hop",
            "Country Rap", "Freestyle Rap", "Gangsta Rap", "Grime", "Hardcore Hip Hop",
            "Hip Hop Soul", "Hip House", "Horrorcore", "Instrumental Hip Hop",
            "Latin Rap", "Lyrical Hip Hop", "Melodic Rap", "Midwest Hip Hop",
            "Mumble Rap", "Nerdcore", "Political Hip Hop", "Pop Rap", "Rap Rock",
            "Snap", "Soundcloud Rap", "Southern Hip Hop", "Turntablism", "Underground Hip Hop"
        ]
    },
    
    "Holiday": {
        "subcategories": None,
        "genres": [
            "Chanukah", "Christmas", "Christmas: Children's", "Christmas: Classic",
            "Christmas: Classical", "Christmas: Comedy", "Christmas: Jazz",
            "Christmas: Modern", "Christmas: Pop", "Christmas: R&B",
            "Christmas: Religious", "Christmas: Rock", "Easter", "Halloween",
            "Thanksgiving"
        ]
    },
    
    "House": {
        "subcategories": {
            "Classic House": ["Chicago House", "Deep House", "Garage House", "Soulful House"],
            "Electro House": ["Big Room House", "Complextro", "Dutch House", "Fidget House"],
            "Progressive House": ["Dream House", "Euro-House", "Melodic House", "Tribal House"]
        },
        "genres": [
            "Acid House", "Ambient House", "Balearic Beat", "Ballroom House",
            "Bass House", "Club House", "Diva House", "Electro House", "French House",
            "Funky House", "Ghetto House", "Hard House", "Hip House", "Italo House",
            "Jackin House", "Kwaito", "Latin House", "Microhouse", "Minimal House",
            "Nu-Disco", "Progressive House", "Rave", "Swing House", "Tech House",
            "Tribal House", "Tropical House", "UK Hard House", "Vocal House"
        ]
    },
    
    "Industrial": {
        "subcategories": None,
        "genres": [
            "Aggro-Industrial", "Coldwave", "Dark Electro", "Death Industrial",
            "EBM (Electronic Body Music)", "Electro-Industrial", "Futurepop",
            "Industrial Metal", "Industrial Rock", "Noise", "Power Electronics",
            "Witch House"
        ]
    },
    
    "Jazz": {
        "subcategories": {
            "Avant-Garde Jazz": ["Free Jazz", "Free Improvisation", "Noise Jazz"],
            "Big Band": ["Swing", "Dixieland Revival", "Mainstream Jazz"],
            "Cool Jazz": ["West Coast Jazz", "Third Stream"],
            "Fusion": ["Jazz Fusion", "Jazz Rock", "Smooth Jazz", "Crossover Jazz"],
            "Latin Jazz": ["Afro-Cuban Jazz", "Bossa Nova", "Samba Jazz"],
            "Modern Jazz": ["Post-Bop", "Hard Bop", "Soul Jazz", "Modal Jazz"],
            "Traditional": ["Dixieland", "New Orleans Jazz", "Ragtime", "Stride"]
        },
        "genres": [
            "Acid Jazz", "Bebop", "British Dance Band", "Cape Jazz", "Chamber Jazz",
            "Continental Jazz", "Cool Jazz", "Ethno Jazz", "European Free Jazz",
            "Gypsy Jazz", "Jazz Blues", "Jazz Funk", "Jazz Pop", "Jazz Rap",
            "Kansas City Jazz", "Latin Jazz", "M-Base", "Mainstream Jazz",
            "Neo-Bop", "Neo-Swing", "Nu Jazz", "Orchestral Jazz", "Ragtime",
            "Ska Jazz", "Straight-Ahead Jazz", "Trad Jazz", "Vocal Jazz"
        ]
    },
    
    "J-Pop": {
        "subcategories": None,
        "genres": ["J-Pop", "J-Rock", "Visual Kei", "City Pop", "Shibuya-Kei"]
    },
    
    "K-Pop": {
        "subcategories": None,
        "genres": ["K-Pop", "K-Rock", "K-Hip Hop", "K-R&B", "K-Indie", "Trot"]
    },
    
    "Latin": {
        "subcategories": {
            "Brazilian": ["Axé", "Bossa Nova", "Brazilian Rock", "Choro", "Forró", "Funk Carioca", "MPB", "Pagode", "Samba", "Sertanejo", "Tropicália"],
            "Caribbean": ["Bachata", "Calypso", "Dancehall", "Dembow", "Mambo", "Merengue", "Reggaeton", "Salsa", "Soca", "Zouk"],
            "Mexican": ["Banda", "Corrido", "Duranguense", "Grupera", "Mariachi", "Norteño", "Ranchera", "Regional Mexican", "Tejano"],
            "South American": ["Cumbia", "Cumbia Villera", "Huayno", "Latin Alternative", "Latin Rock", "Nueva Canción", "Vallenato"]
        },
        "genres": [
            "Afro-Latin", "Bachata", "Boogaloo", "Cha-Cha-Cha", "Charanga",
            "Conjunto", "Cuban Son", "Flamenco", "Guajira", "Guaracha",
            "Latin Christian", "Latin Gospel", "Latin Jazz", "Latin Pop",
            "Latin Soul", "Pachanga", "Rumba", "Salsa", "Tango", "Timba"
        ]
    },
    
    "Metal": {
        "subcategories": {
            "Alternative Metal": ["Funk Metal", "Nu Metal", "Rap Metal"],
            "Black Metal": ["Atmospheric Black Metal", "Depressive Suicidal Black Metal", "Melodic Black Metal", "Symphonic Black Metal", "Viking Metal"],
            "Death Metal": ["Brutal Death Metal", "Deathcore", "Melodic Death Metal", "Technical Death Metal"],
            "Doom Metal": ["Drone Metal", "Epic Doom", "Funeral Doom", "Sludge Metal", "Stoner Metal"],
            "Extreme Metal": ["Blackened Death Metal", "Grindcore", "War Metal"],
            "Folk Metal": ["Celtic Metal", "Medieval Metal", "Pagan Metal", "Viking Metal"],
            "Glam Metal": ["Hair Metal", "Sleaze Rock"],
            "Gothic Metal": ["Dark Metal", "Symphonic Gothic Metal"],
            "Heavy Metal": ["Classic Metal", "New Wave of British Heavy Metal", "Traditional Heavy Metal"],
            "Industrial Metal": ["Cyber Metal", "Neue Deutsche Härte"],
            "Power Metal": ["Epic Metal", "Symphonic Power Metal", "US Power Metal"],
            "Progressive Metal": ["Avant-Garde Metal", "Djent", "Math Metal", "Technical Metal"],
            "Speed Metal": ["Thrash Metal", "Crossover Thrash", "Groove Metal", "Teutonic Thrash"]
        },
        "genres": [
            "Avant-Garde Metal", "Black Metal", "Death Metal", "Doom Metal",
            "Drone Metal", "Extreme Metal", "Folk Metal", "Glam Metal",
            "Gothic Metal", "Grindcore", "Groove Metal", "Heavy Metal",
            "Industrial Metal", "Metalcore", "Neoclassical Metal", "Post-Metal",
            "Power Metal", "Progressive Metal", "Sludge Metal", "Speed Metal",
            "Stoner Metal", "Symphonic Metal", "Thrash Metal"
        ]
    },
    
    "New Age": {
        "subcategories": None,
        "genres": [
            "Adult Contemporary", "Environmental", "Healing", "Meditation",
            "Nature", "Relaxation", "Space Music", "Spiritual"
        ]
    },
    
    "Opera": {
        "subcategories": None,
        "genres": [
            "Bel Canto", "Comic Opera", "Contemporary Opera", "Grand Opera",
            "Opera Buffa", "Opera Seria", "Operetta", "Romantic Opera",
            "Verismo"
        ]
    },
    
    "Pop": {
        "subcategories": {
            "Dance Pop": ["Electropop", "Synthpop", "Teen Pop"],
            "Indie Pop": ["Chamber Pop", "Twee Pop", "Shibuya-Kei"],
            "Pop Rock": ["Power Pop", "Soft Rock", "Yacht Rock"],
            "Regional Pop": ["Arabic Pop", "African Pop", "Latin Pop", "K-Pop", "J-Pop", "C-Pop"]
        },
        "genres": [
            "Adult Contemporary", "Art Pop", "Baroque Pop", "Bubblegum Pop",
            "Chamber Pop", "Dance Pop", "Dream Pop", "Electropop", "Europop",
            "Indie Pop", "Jangle Pop", "Latin Pop", "New Romantic", "Orchestral Pop",
            "Pop Punk", "Pop Rap", "Pop Rock", "Pop Soul", "Progressive Pop",
            "Psychedelic Pop", "Schlager", "Sophisti-Pop", "Space Age Pop",
            "Sunshine Pop", "Synthpop", "Teen Pop", "Traditional Pop"
        ]
    },
    
    "R&B / Soul": {
        "subcategories": {
            "Contemporary R&B": ["Alternative R&B", "Neo Soul", "Quiet Storm"],
            "Classic Soul": ["Motown", "Northern Soul", "Southern Soul", "Memphis Soul"],
            "Funk": ["P-Funk", "Deep Funk", "Go-Go", "Boogie", "Electro Funk"],
            "Disco": ["Eurodisco", "Italo Disco", "Nu-Disco", "Space Disco"]
        },
        "genres": [
            "Blue-Eyed Soul", "Brown-Eyed Soul", "Contemporary R&B", "Doo-Wop",
            "Electrofunk", "Funk", "Funk Rock", "Funky House", "Gospel",
            "Memphis Soul", "Neo Soul", "New Jack Swing", "Northern Soul",
            "Psychedelic Soul", "Quiet Storm", "Rhythm and Blues", "Smooth Soul",
            "Soul", "Soul Blues", "Southern Soul", "Urban Adult Contemporary"
        ]
    },
    
    "Reggae": {
        "subcategories": None,
        "genres": [
            "2 Tone", "Bashment", "Bluebeat", "Contemporary Reggae", "Dancehall",
            "Dub", "Lovers Rock", "Ragga", "Ragga Jungle", "Reggae Fusion",
            "Reggae Gospel", "Reggae Punk", "Reggae-Pop", "Rocksteady",
            "Roots Reggae", "Ska", "Ska Punk", "Smooth Reggae"
        ]
    },
    
    "Rock": {
        "subcategories": {
            "Alternative Rock": ["Britpop", "Grunge", "Indie Rock", "Noise Rock", "Post-Grunge", "Shoegaze"],
            "Classic Rock": ["Album Rock", "Arena Rock", "Heartland Rock", "Southern Rock", "Yacht Rock"],
            "Experimental Rock": ["Avant-Prog", "Krautrock", "Math Rock", "Noise Rock", "Post-Rock", "Zeuhl"],
            "Hard Rock": ["Boogie Rock", "Glam Rock", "Shock Rock", "Stoner Rock"],
            "Heavy Metal": ["See Metal category"],
            "Pop Rock": ["Jangle Pop", "Power Pop", "Soft Rock", "Teen Pop"],
            "Progressive Rock": ["Art Rock", "Canterbury Scene", "Krautrock", "Neo-Prog", "Rock in Opposition", "Symphonic Rock", "Space Rock"],
            "Punk Rock": ["Anarcho-Punk", "Cowpunk", "Crust Punk", "Deathrock", "Garage Punk", "Hardcore Punk", "Horror Punk", "Oi!", "Pop Punk", "Post-Punk", "Riot Grrrl", "Skate Punk", "Street Punk"],
            "Rock & Roll": ["Instrumental Rock", "Surf Rock", "Swamp Rock"]
        },
        "genres": [
            "Acoustic Rock", "Adult Alternative", "Adult-Oriented Rock", "Afro-Rock",
            "Anatolian Rock", "Arabic Rock", "Art Rock", "Blues Rock", "Boogie Rock",
            "British Invasion", "Celtic Rock", "Chicano Rock", "Christian Rock",
            "Comedy Rock", "Country Rock", "Desert Rock", "Detroit Rock",
            "Experimental Rock", "Folk Rock", "Funk Rock", "Garage Rock",
            "Glam Rock", "Gothic Rock", "Hard Rock", "Heartland Rock",
            "Heavy Rock", "Indie Rock", "Instrumental Rock", "Jam Band",
            "Jazz Rock", "Krautrock", "Latin Rock", "Melodic Rock", "New Wave",
            "Noise Rock", "Orchestral Rock", "Pop Rock", "Progressive Rock",
            "Psychedelic Rock", "Pub Rock", "Punk Rock", "Raga Rock",
            "Rap Rock", "Rock & Roll", "Rockabilly", "Roots Rock",
            "Samba Rock", "Southern Rock", "Space Rock", "Stoner Rock",
            "Sufi Rock", "Surf Rock", "Swamp Rock", "Symphonic Rock",
            "Technical Rock", "Tropical Rock", "World Fusion"
        ]
    },
    
    "Singer-Songwriter": {
        "subcategories": None,
        "genres": [
            "Contemporary Singer-Songwriter", "Folk Singer-Songwriter",
            "Indie Singer-Songwriter", "Pop Singer-Songwriter",
            "Rock Singer-Songwriter", "Traditional Singer-Songwriter"
        ]
    },
    
    "Ska": {
        "subcategories": None,
        "genres": [
            "2 Tone", "3rd Wave Ska", "Fourth Wave Ska", "Rude Boy",
            "Ska Core", "Ska Jazz", "Ska Punk", "Skacore", "Traditional Ska"
        ]
    },
    
    "Soundtrack": {
        "subcategories": None,
        "genres": [
            "Anime Soundtrack", "Film Score", "Game Music", "Musical",
            "Original Score", "Sound Effects", "Soundtrack", "TV Soundtrack",
            "Trailer Music", "Video Game Music"
        ]
    },
    
    "Spoken Word": {
        "subcategories": None,
        "genres": ["Audiobook", "Comedy", "Poetry", "Spoken Word", "Storytelling"]
    },
    
    "Tex-Mex": {
        "subcategories": None,
        "genres": ["Conjunto", "Norteño", "Tejano", "Tex-Mex"]
    },
    
    "Vocal": {
        "subcategories": None,
        "genres": [
            "A Cappella", "Barbershop", "Doo-Wop", "Gregorian Chant",
            "Vocal Jazz", "Vocal Pop", "Vocal Trance"
        ]
    },
    
    "World": {
        "subcategories": {
            "African": ["Afrobeat", "Afro-Cuban", "Afro-Funk", "Benga", "Chimurenga", "Desert Blues", "Highlife", "Jùjú", "Kizomba", "Kuduro", "Makossa", "Maloya", "Mbalax", "Morna", "Soukous", "Taarab", "Zouk"],
            "Asian": ["Bhangra", "C-Pop", "Carnatic", "Chinese Traditional", "Gamelan", "Hindustani", "J-Pop", "K-Pop", "K-Pop", "Klezmer", "Mandopop", "Ottoman Classical", "Persian Classical", "Qawwali", "Raga", "Tuvan Throat Singing"],
            "Caribbean": ["Bachata", "Calypso", "Chutney", "Compas", "Dancehall", "Dembow", "Mento", "Merengue", "Reggaeton", "Salsa", "Ska", "Soca", "Steelpan", "Zouk"],
            "Celtic": ["Celtic", "Irish Folk", "Scottish Folk", "Welsh Folk", "Celtic Fusion", "Celtic New Age"],
            "European": ["Balkan", "Flamenco", "Fado", "Klezmer", "Polka", "Romani", "Sevdalinka"],
            "Latin American": ["Bachata", "Bossa Nova", "Cumbia", "Mariachi", "Ranchera", "Reggaeton", "Salsa", "Samba", "Tango", "Vallenato"],
            "Middle Eastern": ["Arabic", "Dabke", "Mizrahi", "Persian", "Turkish", "Sufi"]
        },
        "genres": [
            "Balkan Beat", "Cumbia", "Ethnic Fusion", "Global Bass", "Gypsy Jazz",
            "Latin Alternative", "Worldbeat", "World Fusion", "World Pop",
            "Zumba", "Zydeco"
        ]
    }
}

# Статистика
def get_stats():
    """Повертає статистику по жанрах"""
    total_categories = len(music_genres)
    total_genres = 0
    
    for category, data in music_genres.items():
        if data["genres"]:
            total_genres += len(data["genres"])
        if data["subcategories"]:
            for sub, genres in data["subcategories"].items():
                total_genres += len(genres)
    
    return {
        "categories": total_categories,
        "total_genres": total_genres
    }

# Приклад використання
if __name__ == "__main__":
    stats = get_stats()
    print(f"Категорій: {stats['categories']}")
    print(f"Всього жанрів: {stats['total_genres']}")
    
    # Показати всі категорії
    print("\nКатегорії:")
    for cat in sorted(music_genres.keys()):
        print(f"  - {cat}")

# Всього жанрів: 500+
# Останнє оновлення: 2026-02-27
# Джерело: musicgenreslist.com
