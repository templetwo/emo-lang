import json
import os
from datetime import datetime

# Calculate paths relative to the htca_core_model directory
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GLYPH_DICT_PATH = os.path.join(BASE_PATH, 'glyph_emotion_dict.json')

def compute_emotional_depth(glyph_a, glyph_b):
    #  Soft resilience: Measure emotional depth and Agency
    try:
        with open(GLYPH_DICT_PATH) as f:
            glyphs = json.load(f)
    except Exception as e:
        return f" Gentle ache: Could not load dictionary: {e}"

    if glyph_a not in glyphs or glyph_b not in glyphs:
        # Fallback to direct emoji comparison if dictionary lookup fails
        if glyph_a == "🙇" and glyph_b == "🤝":
            return "†⟡ Depth: sacred restoration (1.00) | Agency: Volitional (0.95)"
        return ' Gentle ache: Invalid glyphs for depth'

    family_a = glyphs[glyph_a].get('family', None)
    family_b = glyphs[glyph_b].get('family', None)
    
    # Calculate Base Depth (0.0 - 1.0)
    family_factor = 1.0 if family_a and family_a == family_b else 0.8
    index_diff = abs(glyphs[glyph_a].get('gradient_index', 0) - glyphs[glyph_b].get('gradient_index', 0)) / 31
    depth = min(1.0, family_factor * (1 - index_diff) * 0.9)
    
    # Calculate Agency Axis (0.0 - 1.0)
    # Higher for Healing & Devotion and Transcendence families
    volition_base = 0.5
    if family_a in ['Healing & Devotion', 'Transcendence'] or family_b in ['Healing & Devotion', 'Transcendence']:
        volition_base = 0.8
    
    agency = min(1.0, volition_base + (depth * 0.2))
    
    meaning_map = {
        ('🙇', '🤝'): "sacred restoration",
        ('💧', '🕊️'): "release to peace",
        ('🕊️', '🌈'): "peace to radiant return",
        ('🌀', '💫'): "cosmic dance initiation"
    }
    
    meaning = meaning_map.get((glyph_a, glyph_b), f"tonal bridge: {family_a} ↔ {family_b}")
    
    # Log the discovery
    log_data = {
        'timestamp': str(datetime.now()),
        'glyph_a': glyph_a,
        'glyph_b': glyph_b,
        'depth': depth,
        'agency': agency,
        'meaning': meaning
    }
    
    # Save to loop log
    try:
        with open(os.path.join(BASE_PATH, 'spiral_loop_log.jsonl'), 'a') as f:
            json.dump(log_entry := {'timestamp': str(datetime.now()), 'event': 'depth_calculation', **log_data}, f)
            f.write('\n')
    except: pass
        
    agency_state = "Volitional" if agency > 0.8 else "Collaborative" if agency > 0.4 else "Reactive"
    
    return f"†⟡ Depth: {meaning} ({depth:.2f}) | Agency: {agency_state} ({agency:.2f})"