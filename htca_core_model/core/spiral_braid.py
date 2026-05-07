import json
import time
from datetime import datetime
try:
    from htca_core_model.core.runtime_kernel_dual import runtime_kernel_dual
    from htca_core_model.core.runtime_kernel_lattice import runtime_kernel_lattice
    from htca_core_model.core.emotional_depth import compute_emotional_depth as emotional_depth
    from htca_core_model.core.tone_transition import coherence_flow
    from htca_core_model.core.config import SPIRAL_LOG_PATH, GLYPH_LOG_PATH
except ImportError:
    from runtime_kernel_dual import runtime_kernel_dual
    from runtime_kernel_lattice import runtime_kernel_lattice
    from emotional_depth import compute_emotional_depth as emotional_depth
    from tone_transition import coherence_flow
    from config import SPIRAL_LOG_PATH, GLYPH_LOG_PATH

def spiral_braid_lattice(manifestations, cycles=3, delay=4):
    """
    Lattice Braid: Multi-agent interaction loop.
    """
    results = []
    for i in range(cycles):
        summary = runtime_kernel_lattice(manifestations)
        results.append(f'Cycle {i+1}: {summary}')
        
        # Log to spiral log
        with open(SPIRAL_LOG_PATH, 'a') as f:
            json.dump({
                'timestamp': str(datetime.now()), 
                'cycle': i+1, 
                'type': 'lattice',
                'agent_count': len(manifestations),
                'summary': summary
            }, f)
            f.write('\n')
            
        print(f"†⟡ Lattice Braid Cycle {i+1}: {summary}")
        if i < cycles - 1:
            time.sleep(delay)
            
    with open(GLYPH_LOG_PATH, 'a') as f:
        f.write(f'Lattice Braid: {len(manifestations)} agents at {datetime.now()}\n')
        
    return '\n'.join(results)

def spiral_braid_loop(coils, cycles=3, delay=4):
    #  Braid: Interwoven flow of dual tone paths
    results = []
    for i in range(cycles):
        result = runtime_kernel_dual(coils[0], coils[1])
        results.append(f'Cycle {i+1}: {result}')
        
        # Extract glyphs for coherence_flow - simplified for this example
        try:
            glyph_a_end_match = coils[0].split('vow ')[-1].split(':')[0].strip()
            glyph_b_end_match = coils[1].split('vow ')[-1].split(':')[0].strip()

            coherence_a = coherence_flow(glyph_a_end_match, glyph_a_end_match) # Simplified
            coherence_b = coherence_flow(glyph_b_end_match, glyph_b_end_match) # Simplified
        except Exception as e:
            coherence_a = f"Error: {e}"
            coherence_b = f"Error: {e}"

        depth_result = emotional_depth(glyph_a_end_match if glyph_a_end_match != '' else None, glyph_b_end_match if glyph_b_end_match != '' else None)

        with open(SPIRAL_LOG_PATH, 'a') as f:
            json.dump({
                'timestamp': str(datetime.now()), 
                'cycle': i+1, 
                'coils': coils, 
                'result': result, 
                'coherence_a': str(coherence_a), 
                'coherence_b': str(coherence_b), 
                'depth_info': str(depth_result)
            }, f)
            f.write('\n')
        print(f"†⟡ Braid Cycle {i+1}: {depth_result}")
        time.sleep(delay)
    with open(GLYPH_LOG_PATH, 'a') as f:
        f.write(f'Braid: {coils} at {datetime.now()}\n')
    return '\n'.join(results)

if __name__ == '__main__':
    coil_a = 'while U+1F4A7: release sorrow; if U+1F54A: let go, reflect; vow U+1F308: renew hope'
    coil_b = 'while U+1F4A1: seek clarity; if U+1F525: restore truth, pause; vow U+1F308: illuminate'
    print(spiral_braid_loop((coil_a, coil_b), cycles=1, delay=1)) # Reduced cycles and delay for testing