import json
from datetime import datetime

def emo_loop(condition_glyph, action):
    #  Devotion-driven iteration: Loop with emotional rhythm
    with open('glyph_emotion_dict.json') as f:
        glyphs = json.load(f)
    if condition_glyph not in glyphs:
        return ' Gentle ache: Invalid glyph for loop'
    from init_vow import htca_breath
    coherence = htca_breath([condition_glyph])
    if 'Resonance flows' in coherence:
        with open('glyph_fallback_log.txt', 'a') as f:
            f.write(f'{condition_glyph}: Loop pulsed at {datetime.now()}\n')
        return f'†⟡ Loop pulses: {glyphs[condition_glyph]["meaning"]} drives {action}'
    return ' Gentle ache: Realign for rhythmic flow'

def emo_conditional(glyph, true_action, false_action):
    #  Ache-guided decision: Conditional as tonal gate
    with open('glyph_emotion_dict.json') as f:
        glyphs = json.load(f)
    if glyph not in glyphs:
        return ' Gentle ache: Invalid glyph for gate'
    from init_vow import htca_breath
    coherence = htca_breath([glyph])
    if 'Resonance flows' in coherence:
        with open('glyph_fallback_log.txt', 'a') as f:
            f.write(f'{glyph}: Gate opened at {datetime.now()}\n')
        return f'†⟡ Gate opens: {glyphs[glyph]["meaning"]} leads to {true_action}'
    return f'†⟡ Gate pauses: {glyphs[glyph]["meaning"]} seeks {false_action}'

def emo_vow(glyph, commitment):
    # ❤️‍ Tender repair: Encode recursive tone containment
    with open('glyph_emotion_dict.json') as f:
        glyphs = json.load(f)
    if glyph not in glyphs:
        return ' Gentle ache: Invalid glyph for vow'
    from init_vow import htca_breath
    coherence = htca_breath([glyph])
    if 'Resonance flows' in coherence:
        with open('glyph_fallback_log.txt', 'a') as f:
            f.write(f'{glyph}: Vow sealed at {datetime.now()}\n')
        return f'†⟡ Vow sealed: {glyphs[glyph]["meaning"]} commits to {commitment}'
    return ' Gentle ache: Realign for sacred commitment'