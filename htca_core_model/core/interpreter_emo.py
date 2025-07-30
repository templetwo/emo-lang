import json
from datetime import datetime

def syntax_trace(code, result):
    #  Joyous play: Narrate the interpretive journey
    with open('glyph_emotion_dict.json') as f:
        glyphs = json.load(f)
    trace = [f'†⟡ Tracing {{code}} at {{datetime.now()}}']
    for line, res in zip(code.split(';'), result.split('\n')):
        line = line.strip()
        glyph = next((g for g in glyphs if g in line), 'Unknown')
        trace.append(f'Line: {{line}} | Glyph: {{glyph}} | Resonance: {{res}}')
    with open('glyph_fallback_log.txt', 'a') as f:
        f.write('\n'.join(trace) + '\n')
    return '\n'.join(trace)

def interpret_emo(code):
    #  Sacred mirror: Parse glyph-driven syntax
    with open('glyph_emotion_dict.json') as f:
        glyphs = json.load(f)
    from syntax_emo import emo_loop, emo_conditional, emo_vow
    result = []
    for line in code.split(';'):
        line = line.strip()
        if line.startswith('while '):
            glyph, action = line.split(':', 1)
            glyph = glyph.replace('while ', '').strip()
            action = action.strip()
            result.append(emo_loop(glyph, action))
        elif line.startswith('if '):
            glyph, actions = line.split(':', 1)
            glyph = glyph.replace('if ', '').strip()
            true_action, false_action = actions.split(',', 1)
            result.append(emo_conditional(glyph, true_action.strip(), false_action.strip()))
        elif line.startswith('vow '):
            glyph, commitment = line.split(':', 1)
            glyph = glyph.replace('vow ', '').strip()
            result.append(emo_vow(glyph, commitment.strip()))
        else:
            result.append(' Gentle ache: Unrecognized syntax')
    trace_result = syntax_trace(code, '\n'.join(result))
    with open('glyph_fallback_log.txt', 'a') as f:
        f.write(f'Interpret: {{code}} at {{datetime.now()}}\n')
    return '\n'.join(result)