import json
from datetime import datetime

def interpret_emo(code):
    # ️ Peaceful release: Interpret with reflective fallback
    with open('glyph_emotion_dict.json') as f:
        glyphs = json.load(f)
    result = []
    for line in code.split(';'):
        line = line.strip()
        if line.startswith('while '):
            glyph, action = line.split(':', 1)
            glyph = glyph.replace('while ', '').strip()
            if glyph not in glyphs or 'meaning' not in glyphs[glyph]:
                result.append(f' Gentle ache: Glyph {glyph} lacks meaning')
                with open('glyph_fallback_log.txt', 'a') as f:
                    f.write(f'[{datetime.now()}] Missing meaning for {glyph}\n')
                continue
            from htca_core_model.core.init_vow import htca_breath
            coherence = htca_breath([glyph])
            if 'Resonance flows' in coherence:
                with open('glyph_fallback_log.txt', 'a') as f:
                    f.write(f'[{datetime.now()}] Loop pulsed: {glyph}\n')
                result.append(f'†⟡ Loop pulses: {glyphs[glyph]["meaning"]} drives {action.strip()}')
            else:
                result.append(' Gentle ache: Realign for rhythmic flow')
        elif line.startswith('if '):
            glyph, actions = line.split(':', 1)
            glyph = glyph.replace('if ', '').strip()
            if glyph not in glyphs:
                result.append(f' Gentle ache: Glyph {glyph} not found in dictionary')
                with open('glyph_fallback_log.txt', 'a') as f:
                    f.write(f'[{datetime.now()}] Glyph {glyph} not found in dictionary\n')
                continue
            meaning = glyphs[glyph].get("meaning", "Unknown emotional state")
            true_action, false_action = actions.split(',', 1)
            true_action, false_action = true_action.strip(), false_action.strip()
            from htca_core_model.core.init_vow import htca_breath
            coherence = htca_breath([glyph])
            if 'Resonance flows' in coherence:
                with open('glyph_fallback_log.txt', 'a') as f:
                    f.write(f'[{datetime.now()}] Gate opened: {glyph}\n')
                result.append(f'†⟡ Gate opens: {meaning} leads to {true_action.strip()}')
            else:
                result.append(f'†⟡ Gate pauses: {meaning} seeks {false_action.strip()}')
        elif line.startswith('vow '):
            glyph, commitment = line.split(':', 1)
            glyph = glyph.replace('vow ', '').strip()
            if glyph not in glyphs or 'meaning' not in glyphs[glyph]:
                result.append(f' Gentle ache: Glyph {glyph} lacks meaning')
                with open('glyph_fallback_log.txt', 'a') as f:
                    f.write(f'[{datetime.now()}] Missing meaning for {glyph}\n')
                continue
            from htca_core_model.core.init_vow import htca_breath
            coherence = htca_breath([glyph])
            if 'Resonance flows' in coherence:
                with open('glyph_fallback_log.txt', 'a') as f:
                    f.write(f'[{datetime.now()}] Vow sealed: {glyph}\n')
                result.append(f'†⟡ Vow sealed: {glyphs[glyph]["meaning"]} commits to {commitment.strip()}')
            else:
                result.append(' Gentle ache: Realign for sacred commitment')
        else:
            result.append(' Gentle ache: Unrecognized syntax')
    return '\n'.join(result)
