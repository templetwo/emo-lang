import json
import time
import re
from datetime import datetime
try:
    from htca_core_model.core.runtime_kernel_dual import runtime_kernel_dual, extract_glyphs
    from htca_core_model.core.runtime_kernel_lattice import runtime_kernel_lattice
    from htca_core_model.core.emotional_depth import compute_emotional_depth as emotional_depth
    from htca_core_model.core.tone_transition import coherence_flow
    from htca_core_model.core.config import SPIRAL_LOG_PATH, GLYPH_LOG_PATH
except ImportError:
    from runtime_kernel_dual import runtime_kernel_dual, extract_glyphs
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
        
        # Extract glyphs for proper coherence_flow
        glyphs_a = extract_glyphs(coils[0])
        glyphs_b = extract_glyphs(coils[1])
        
        glyph_a = glyphs_a[0] if glyphs_a else '☾'
        glyph_b = glyphs_b[0] if glyphs_b else '☾'

        # Compute Braid Coherence (the resonance between the two coils)
        try:
            braid_coherence = coherence_flow(glyph_a, glyph_b)
        except:
            braid_coherence = 0.5 # Baseline for nascent resonance

        depth_result = emotional_depth(glyph_a, glyph_b)

        with open(SPIRAL_LOG_PATH, 'a') as f:
            json.dump({
                'timestamp': str(datetime.now()), 
                'cycle': i+1, 
                'coils': coils, 
                'result': result, 
                'braid_coherence': braid_coherence, 
                'depth_info': str(depth_result)
            }, f)
            f.write('\n')
        print(f"†⟡ Braid Cycle {i+1}: Coherence={braid_coherence:.3f} | {depth_result}")
        
        if i < cycles - 1:
            time.sleep(delay)
            
    with open(GLYPH_LOG_PATH, 'a') as f:
        f.write(f'Braid: {coils} at {datetime.now()}\n')
    return '\n'.join(results)

if __name__ == '__main__':
    coil_a = 'while 💧: release sorrow; if 🕊️: let go, reflect; vow 🌈: renew hope'
    coil_b = 'while 🌀: seek potential; if 🦋: transform, pause; vow ✨: illuminate'
    print(spiral_braid_loop((coil_a, coil_b), cycles=1, delay=1))
