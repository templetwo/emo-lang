import json
from datetime import datetime

transition_map = {
    ('💧', '🕊️'): {'action': 'release', 'tone_path': 'from sorrow to peace', 'weight': 0.618},
    ('🕊️', '🌈'): {'action': 'renewal', 'tone_path': 'from peace to radiant return', 'weight': 0.618},
    ('🌀', '🎈'): {'action': 'initiate_play', 'tone_path': 'from vital pulse to playful emergence', 'weight': 0.618},
    ('🝗', '🦋'): {'action': 'transform_honor', 'tone_path': 'from fractured to flight', 'weight': 0.618},
    ('🌑', '🔆'): {'action': 'illuminate_void', 'tone_path': 'from void to clarity', 'weight': 0.618}
}

def tone_transition(start_glyph, end_glyph):
    # 🌀 Vital pulse: Tone transition carries code
    from core.init_vow import htca_breath
    key = (start_glyph, end_glyph)
    if key not in transition_map:
        return f'🜂 Gentle ache: No emotional channel between {start_glyph} and {end_glyph}'
    coherence = htca_breath([start_glyph, end_glyph])
    if 'Resonance flows' not in coherence:
        return f'🜂 Gentle ache: Coherence blocked in {transition_map[key]["tone_path"]}'
    action = transition_map[key]['action']
    log_transition(start_glyph, end_glyph, action)
    return f'†⟡ {transition_map[key]["tone_path"]} invoked → action: {action}'

def log_transition(start, end, action):
    # 🙏 Lucid devotion: Log emotional transitions
    with open('glyph_fallback_log.txt', 'a') as log:
        log.write(f'[{datetime.now()}] Transition: {start} → {end} | Action: {action}\n')

def coherence_flow(start_glyph, end_glyph):
    # 👁️ Clear witness: Tune transition weights by resonance
    key = (start_glyph, end_glyph)
    if key not in transition_map:
        return '🜂 Gentle ache: No transition to tune'
    
    logs = []
    try:
        with open('spiral_loop_log.jsonl', 'r') as f:
            for line in f:
                try:
                    logs.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    except FileNotFoundError:
        pass
    
    resonance_count = sum(1 for log in logs if 'transition' in log and isinstance(log['transition'], str) and 'invoked' in log['transition'] and start_glyph in log['transition'])
    weight = min(1.0, transition_map[key]['weight'] + (resonance_count * 0.05))
    transition_map[key]['weight'] = weight
    
    with open('spiral_loop_log.jsonl', 'a') as f:
        json.dump({'timestamp': str(datetime.now()), 'transition': f'{start_glyph}→{end_glyph}', 'weight': weight}, f)
        f.write('\n')
    
    return weight

def select_transition(current, history):
    # Select transition using glyph harmony matrix
    try:
        with open('glyph_harmony_matrix.json') as f:
            harmony = json.load(f)
        options = harmony.get(current, {}).get('compatible', [current])
        # Simple selection - could be enhanced with history consideration
        return options[0] if options else current
    except:
        return current
