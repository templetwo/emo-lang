import json
from datetime import datetime

def log_emotion(code, glyph, result):
    # ️ Gentle vigil: Log emotional transitions with formatted f-strings
    with open('glyph_emotion_dict.json') as f:
        glyphs = json.load(f)
    glyph_meaning = glyphs.get(glyph, {}).get('meaning', 'Unknown')
    with open('spiral_loop_log.jsonl', 'a') as f:
        json.dump({'timestamp': str(datetime.now()), 'code': code, 'glyph': glyph, 'meaning': glyph_meaning, 'result': result}, f)
        f.write('\n')
    with open('glyph_fallback_log.txt', 'a') as f:
        f.write(f'[{datetime.now()}] Tracing {code} | Glyph: {glyph} | Resonance: {result}\n')
    return f'†⟡ Tracing {code} at {datetime.now()}'

