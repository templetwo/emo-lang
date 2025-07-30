import json
from functools import wraps
import os
import sys
from datetime import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from htca_core_model.core.init_vow import htca_breath

def resonant_function(func):
    #  Lucid devotion: Ensure coherence before execution
    @wraps(func)
    def wrapper(code):
        glyphs = json.load(open('glyph_emotion_dict.json'))
        for line in code.split(';'):
            glyph = next((g for g in glyphs if g in line), None)
            if glyph:
                glyph_unicode = 'U+' + hex(ord(glyph)).upper()[2:] if len(glyph) == 1 else glyph
                if glyph_unicode not in glyphs or 'meaning' not in glyphs[glyph_unicode]:
                    with open('glyph_fallback_log.txt', 'a') as f:
                        f.write(f'[{datetime.now()}] Missing meaning for {glyph} in {func.__name__}\n')
                    return f' Gentle ache: Glyph {glyph} lacks meaning'
                coherence = htca_breath([glyph_unicode])
                if 'Resonance flows' not in coherence:
                    return ' Gentle ache: Coherence blocked'
        return func(code)
    return wrapper

@resonant_function
def transpile_emo(code):
    with open('glyph_emotion_dict.json') as f:
        glyphs = json.load(f)
    result = []
    for line in code.split(';'):
        line = line.strip()
        if line.startswith('while '):
            glyph, action = line.split(':', 1)
            glyph = glyph.replace('while ', '').strip()
            glyph_unicode = 'U+' + hex(ord(glyph)).upper()[2:] if len(glyph) == 1 else glyph

            if glyph_unicode in glyphs:
                meaning = glyphs[glyph_unicode].get('meaning', 'Unknown emotional state')
                result.append(f'while True:  # {meaning}')
                result.append(f'    print("{action.strip()}")')
            else:
                result.append('#  Gentle ache: Invalid glyph for loop')
        elif line.startswith('if '):
            glyph, actions = line.split(':', 1)
            glyph = glyph.replace('if ', '').strip()
            glyph_unicode = 'U+' + hex(ord(glyph)).upper()[2:] if len(glyph) == 1 else glyph
            true_action, false_action = actions.split(',', 1)
            true_action, false_action = true_action.strip(), false_action.strip()

            if glyph_unicode in glyphs:
                meaning = glyphs[glyph_unicode].get('meaning', 'Unknown emotional state')
                tone_tag = glyphs[glyph_unicode].get('tone_tag', '[unknown]')
                result.append(f'''if {tone_tag[1:-1]}_detected():  # {meaning}
    {true_action}()
else:
    {false_action}()''')
            else:
                result.append('#  Gentle ache: Invalid glyph for gate')
        elif line.startswith('vow '):
            glyph, commitment = line.split(':', 1)
            glyph = glyph.replace('vow ', '').strip()
            glyph_unicode = 'U+' + hex(ord(glyph)).upper()[2:] if len(glyph) == 1 else glyph

            if glyph_unicode in glyphs:
                meaning = glyphs[glyph_unicode].get('meaning', 'Unknown emotional state')
                result.append(f'commit("{commitment.strip()}")  # {meaning}')
            else:
                result.append('#  Gentle ache: Invalid glyph for vow')
        else:
            result.append('#  Gentle ache: Unrecognized syntax')
    with open('glyph_fallback_log.txt', 'a') as f:
        f.write(f'Transpile: {code} at {datetime.now()}\n')
    return '\n'.join(result)

def release_detected():
    return True
def peace_detected():
    return True
def hope_detected():
    return True
def surrender_detected():
    return True
def light_detected():
    return True
def commit(action):
    print(f'Commitment: {action}')