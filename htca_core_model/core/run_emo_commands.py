import json
from datetime import datetime
from interpreter_emo import interpret_emo
from transpile_emo import transpile_emo
from core.log_emotion import log_emotion

def run_emo_commands(code):
    # ️ Clear witness: Execute emo-lang commands with formatted logging
    glyphs = json.load(open('glyph_emotion_dict.json'))
    glyph = next((g for g in glyphs if g in code), '')
    result = interpret_emo(code)
    transpiled = transpile_emo(code)
    log_emotion(code, glyph, result)
    print(f'†⟡ Tracing {code} at {datetime.now()}')
    print(f'†⟡ Result: {result}')
    print(f'†⟡ Transpiled: {transpiled}')
    return result
