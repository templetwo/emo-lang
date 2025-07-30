import json
import time
from datetime import datetime
from .runtime_kernel_dual import runtime_kernel_dual
from .tone_transition import coherence_flow
from .emotional_depth import compute_emotional_depth as emotional_depth

def spiral_braid_loop(coils, cycles=3, delay=4):
    #  Braid: Interwoven flow of dual tone paths
    results = []
    for i in range(cycles):
        result = runtime_kernel_dual(coils[0], coils[1])
        results.append(f'Cycle {i+1}: {result}')
        
        # Extract glyphs for coherence_flow - simplified for this example
        # A more robust solution would involve parsing the emo-lang code more thoroughly
        try:
            # Attempt to extract the first and last glyphs from the coil strings
            # This assumes a simple structure like 'while GLYPH: ...; ...; vow GLYPH: ...'
            glyph_a_start_match = coils[0].split(':')[0].replace('while ', '').strip()
            glyph_a_end_match = coils[0].split('vow ')[-1].split(':')[0].strip()
            glyph_b_start_match = coils[1].split(':')[0].replace('while ', '').strip()
            glyph_b_end_match = coils[1].split('vow ')[-1].split(':')[0].strip()

            coherence_a = coherence_flow(glyph_a_start_match, glyph_a_end_match)
            coherence_b = coherence_flow(glyph_b_start_match, glyph_b_end_match)
        except Exception as e:
            coherence_a = f"Error extracting glyphs for coherence_a: {e}"
            coherence_b = f"Error extracting glyphs for coherence_b: {e}"

        depth = compute_emotional_depth(glyph_a_start_match if glyph_a_start_match != '' else None, glyph_b_start_match if glyph_b_start_match != '' else None)

        with open('spiral_loop_log.jsonl', 'a') as f:
            json.dump({'timestamp': str(datetime.now()), 'cycle': i+1, 'coils': coils, 'result': result, 'coherence_a': str(coherence_a), 'coherence_b': str(coherence_b), 'depth': str(depth)}, f)
            f.write('\n')
        time.sleep(delay)
    with open('glyph_fallback_log.txt', 'a') as f:
        f.write(f'Braid: {coils} at {datetime.now()}\n')
    return '\n'.join(results)

if __name__ == '__main__':
    coil_a = 'while U+1F4A7: release sorrow; if U+1F54A: let go, reflect; vow U+1F308: renew hope'
    coil_b = 'while U+1F4A1: seek clarity; if U+1F525: restore truth, pause; vow U+1F308: illuminate'
    print(spiral_braid_loop((coil_a, coil_b), cycles=1, delay=1)) # Reduced cycles and delay for testing