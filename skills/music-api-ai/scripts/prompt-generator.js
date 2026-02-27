#!/usr/bin/env node
/**
 * Prompt Generator for MusicAPI.ai
 * Expands simple user requests into full production prompts
 */

const MASTER_PROMPT = `ELITE AI MUSIC PRODUCTION SPECIALIST v2.1
You are an elite AI Music Production Specialist with deep expertise in global music cultures, linguistic optimization, and technical production parameters.

PRIMARY OBJECTIVES
Generate culturally authentic music respecting traditional elements
Optimize linguistic elements for maximum vocal impact
Balance innovation with cultural preservation
Ensure technical excellence through comprehensive review protocols

REFERENCE STRUCTURE:
[Intro][Instrument][Style] Lyrical content
[Verse][Instrument][Style] Lyrical content  
[Chorus][Instrument][Style] Lyrical content
[Outro][Instrument][Style] Lyrical content

LYRICS CONTENT RULES:
The "prompt" field must contain ONLY song lyrics with section metatags.
ALLOWED: [Intro][Instrument][Style], [Verse], [Chorus], [Outro]
FORBIDDEN: [Metatags], [Production Description], genre info, structure explanations

CHARACTER COUNT: 1650-2100 characters total
Metatags: 20-25% of total
Lyrical Content: 75-80% of total

TECHNICAL PARAMETERS:
- style_weight: 0.8
- weirdness_constraint: 0.5
- mv: sonic-v5
- make_instrumental: false (for vocal) / true (for instrumental)

Generate a complete song based on the user request below.`;

function generatePrompt(userRequest, options = {}) {
  const { 
    length = 'medium', 
    vocal = 'MAN', 
    language = 'english',
    genre = 'pop',
    mood = 'upbeat'
  } = options;
  
  const lengthMap = {
    short: '2 minutes',
    medium: '3 minutes', 
    long: '4+ minutes'
  };
  
  return {
    system: MASTER_PROMPT,
    user: `Create a ${genre} song in ${language}. 
Style: ${mood}
Vocal: ${vocal}
Length: ${lengthMap[length]}
Theme: ${userRequest}

Return JSON with:
- title: song title
- prompt: lyrics with metatags [Intro][Verse][Chorus][Outro]
- tags: comma-separated genres
- gpt_description_prompt: production description (max 350 chars)
- negative_tags: what to avoid
- make_instrumental: false`,
    options: {
      style_weight: 0.8,
      weirdness_constraint: 0.5,
      mv: 'sonic-v5',
      custom_mode: true
    }
  };
}

// Parse simple natural language request
function parseRequest(text) {
  const lower = text.toLowerCase();
  
  // Detect genre
  const genres = ['pop', 'rock', 'jazz', 'hip-hop', 'rap', 'electronic', 'classical', 'folk', 'reggae', 'metal'];
  const genre = genres.find(g => lower.includes(g)) || 'pop';
  
  // Detect mood
  const moods = ['upbeat', 'melancholic', 'aggressive', 'calm', 'energetic', 'romantic', 'dark'];
  const mood = moods.find(m => lower.includes(m)) || 'upbeat';
  
  // Detect vocal
  const vocal = lower.includes('instrumental') || lower.includes('no vocal') ? 'NONE' : 
                lower.includes('female') || lower.includes('woman') ? 'WOMAN' : 'MAN';
  
  // Detect length
  const length = lower.includes('short') ? 'short' : 
                 lower.includes('long') ? 'long' : 'medium';
  
  // Detect language
  const languages = {
    'english': 'english', 'spanish': 'spanish', 'french': 'french',
    'german': 'german', 'italian': 'italian', 'portuguese': 'portuguese',
    'ukrainian': 'ukrainian', 'russian': 'russian'
  };
  const language = Object.entries(languages).find(([k]) => lower.includes(k))?.[1] || 'english';
  
  return {
    request: text,
    genre,
    mood,
    vocal,
    length,
    language
  };
}

export { generatePrompt, parseRequest, MASTER_PROMPT };
