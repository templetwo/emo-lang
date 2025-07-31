import json
import time
from datetime import datetime
from core.runtime_kernel_dual import runtime_kernel_dual
from core.tone_transition import coherence_flow
from core.emotional_depth import compute_emotional_depth
from core.init_vow import htca_breath

class SpiralLoop:
    def __init__(self):
        self.pulse_interval = 4.0

def spiral_manifestation_loop(coils, cycles=3, delay=4, coherence_threshold=0.618, base_interval=4):
    # 🧶 Braid: Interwoven flow of dual tone paths
    results = []
    spiral_loop = SpiralLoop()
    spiral_loop.pulse_interval = base_interval
    
    for i in range(cycles):
        result = runtime_kernel_dual(coils[0], coils[1])
        
        # Extract glyphs from coils
        with open('glyph_emotion_dict.json') as f:
            glyph_dict = json.load(f)
        
        glyphs_a = [g for g in glyph_dict.keys() if g in coils[0]]
        glyphs_b = [g for g in glyph_dict.keys() if g in coils[1]]
        current_glyph_sequence = glyphs_a + glyphs_b
        
        # HTCA Validation
        coherence_result = htca_breath(current_glyph_sequence, coherence_threshold)
        coherence_numeric = 0.8 if 'Resonance flows' in coherence_result else 0.3
        
        if coherence_numeric < coherence_threshold:
            log_htca_failure(current_glyph_sequence)
            alternate_result = attempt_alternate_transition(coils)
            results.append(f'Cycle {i+1}: {alternate_result} (realigned)')
            continue
        
        # Calculate coherence flow
        coherence_a = coherence_flow(glyphs_a[0], glyphs_a[-1]) if glyphs_a else '🜂 No glyphs in coil_a'
        coherence_b = coherence_flow(glyphs_b[0], glyphs_b[-1]) if glyphs_b else '🜂 No glyphs in coil_b'
        
        # Compute emotional depth
        depth = compute_emotional_depth(glyphs_a[0] if glyphs_a else '🜂', glyphs_b[0] if glyphs_b else '🜂')
        
        # Dynamic pulse modulation
        spiral_loop.pulse_interval = base_interval * (1.5 - coherence_numeric)
        
        results.append(f'Cycle {i+1}: {result}')
        
        # Log to spiral loop
        with open('spiral_loop_log.jsonl', 'a') as f:
            json.dump({
                'timestamp': str(datetime.now()), 
                'cycle': i+1, 
                'coils': coils, 
                'result': result, 
                'coherence_a': coherence_a, 
                'coherence_b': coherence_b, 
                'depth': depth,
                'htca_coherence': coherence_numeric
            }, f)
            f.write('\n')
        
        time.sleep(spiral_loop.pulse_interval)
    
    # Final logging
    with open('glyph_fallback_log.txt', 'a') as f:
        f.write(f'Braid: {coils} at {datetime.now()}\n')
    
    return '\n'.join(results)

def log_htca_failure(sequence):
    # 🧶 Braid: Log coherence failure
    with open('glyph_fallback_log.txt', 'a') as f:
        f.write(f'[{datetime.now()}] HTCA Coherence failure in {sequence}\n')

def attempt_alternate_transition(coils):
    # 🧶 Braid: Attempt alternate emotional transition
    try:
        with open('glyph_harmony_matrix.json') as f:
            harmony = json.load(f)
        
        # Extract first glyph from first coil
        first_glyph = coils[0].split(':', 1)[0].replace('while ', '').strip()
        compatible_glyphs = harmony.get(first_glyph, {}).get('compatible', [first_glyph])
        
        if compatible_glyphs and compatible_glyphs[0] != first_glyph:
            alternate_glyph = compatible_glyphs[0]
            alternate_coil = coils[0].replace(first_glyph, alternate_glyph)
            return f'†⟡ Realigned: {alternate_glyph} → {runtime_kernel_dual(alternate_coil, coils[1])}'
        else:
            return '🜂 Gentle ache: No compatible realignment found'
    except Exception as e:
        return f'🜂 Gentle ache: Realignment failed - {str(e)}'

if __name__ == '__main__':
    coil_a = 'while 💧: release sorrow; if 🕊️: let go; vow 🌈: renew hope'
    coil_b = 'while 🌑: seek clarity; if 🝗: restore truth; vow 🔆: illuminate'
    print(spiral_manifestation_loop((coil_a, coil_b), cycles=5, delay=6))
