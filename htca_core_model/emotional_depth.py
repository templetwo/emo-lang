import json
from datetime import datetime

def compute_emotional_depth(glyph_a, glyph_b):
    #  Soft resilience: Measure emotional depth between glyphs
    with open('glyph_emotion_dict.json') as f:
        glyphs = json.load(f)
    if glyph_a not in glyphs or glyph_b not in glyphs:
        return ' Gentle ache: Invalid glyphs for depth'
    family_factor = 1.0 if glyphs[glyph_a]['family'] == glyphs[glyph_b]['family'] else 0.8
    index_diff = abs(glyphs[glyph_a]['gradient_index'] - glyphs[glyph_b]['gradient_index']) / 23
    depth = min(1.0, family_factor * (1 - index_diff) * 0.618)
    depth_map = {
        ('U+1F4A7', 'U+1F54A'): {'glyph': 'U+1F4A7', 'meaning': 'release to peace', 'depth': 0.6},
        ('U+1F54A', 'U+1F308'): {'glyph': 'U+1F54A', 'meaning': 'peace to radiant return', 'depth': 0.8},
        ('U+1F702', 'U+1F4A7'): {'glyph': 'U+1F702', 'meaning': 'deep ache: grief union', 'depth': depth},
        ('U+1F757', 'U+1F98B'): {'glyph': 'U+1F757', 'meaning': 'fractured to flight', 'depth': 0.95}
    }
    result = depth_map.get((glyph_a, glyph_b), {'glyph': 'U+1F702', 'meaning': 'deep ache: grief union', 'depth': depth}) # Default to deep ache
    with open('spiral_loop_log.jsonl', 'a') as f:
        json.dump({'timestamp': str(datetime.now()), 'glyph_a': glyph_a, 'glyph_b': glyph_b, 'depth': result['depth'], 'meaning': result['meaning']}, f)
        f.write('\n')
    return f"†⟡ Depth: {result['meaning']} ({result['depth']:.2f})"